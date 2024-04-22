from datetime import datetime
from functools import reduce
import numpy as np
import pandas as pd
import sys


######################## GLOBALS ########################

DATE_FORMATS = [
    '%d.%m.%Y',
    '%d-%m-%Y',
    '%d/%m/%Y',
]
NULL_STRINGS = {"nan", "NAN", "NaN", "null", "Null", "NULL"}


######################## COMMON ########################

def _convert(col: np.array, convert_fn) -> np.array:
    '''
    Helper that takes in an np array (generally raw strings from the CSV) and
    converts it to the specified type or None via convert_fn
    '''
    converted = np.array([
        convert_fn(val)
        for val in col
    ])
    are_nones = pd.isnull(converted)
    not_nones = np.logical_not(are_nones)
    not_none_values = converted[not_nones]
    return are_nones, not_nones, not_none_values


def _clean_continuous__inplace(col: np.array, convert_fn) -> np.array:
    '''
    Helper that takes in an np array (generally raw strings from the CSV) and
    cleans it by drawing values for empty/problematic cells from a normal distribution
    formed by the other cells' value
    '''
    are_nones, not_nones, not_none_values = _convert(col, convert_fn)

    # if thare are not any non_nones, would get divide by 0 error, so check
    mu, sigma = 0, 0
    if not_nones.sum():
        mu, sigma = not_none_values.mean(), not_none_values.std()
    col[are_nones] = np.random.normal(mu, sigma, size=are_nones.sum())
    col[not_nones] = not_none_values
    return col


######################## CATEGORICAL ########################

def _convert_int_or_null(val: str) -> int | None:
    try:
        return int(val)
    except Exception:
        return None


def clean_categorical__inplace(col: np.array) -> np.array:
    are_nones, not_nones, not_none_values = _convert(col, _convert_int_or_null)

    total = not_nones.sum()
    if not total:
        uniques, percentages = [0], [1]
        
    else:
        uniques, counts = np.unique(not_none_values, return_counts=True)
        percentages = [c/total for c in counts]

    col[are_nones] = np.random.choice(uniques, p=percentages)
    col[not_nones] = not_none_values
    return col


######################## NUMERIC ########################

def _convert_float_or_null(val: str) -> float | None:
    try:
        return float(val)
    except Exception:
        return None

def clean_numerical__inplace(col: np.array) -> np.array:
    _clean_continuous__inplace(col, _convert_float_or_null)


######################## DATE OR TIME ########################

def _convert_to_datetimems_or_none(val: str) -> float | None:
    # dataset had whitespace... argh
    val = val.strip()

    # is a time H:M:S,junk
    if ":" in val:
        # only keep 3 time parts HMS
        els = val.split(':')[:3]
    
        def _convert_to_seconds(accum: int, cur: str):
            # sometimes had other data after seconds, not necessary, only keep two digits 
            return (accum*60)+int(cur[:2])
        
        return reduce(_convert_to_seconds, els, 1/60)

    # is a date
    for format in DATE_FORMATS:
        try:
            return datetime.strptime(val, format).timestamp()
        except Exception:
            pass

    return None

def clean_datetime__inplace(col: np.array) -> np.array:
    _clean_continuous__inplace(col, _convert_to_datetimems_or_none)


######################## CHARACTER ########################

def _convert_to_str_or_none(val):
    return None if (val in NULL_STRINGS or val is None) else val


def clean_character__inplace(col: np.array) -> np.array:
    are_nones, _, _ = _convert(col, _convert_to_str_or_none)
    col[are_nones] = np.repeat([""], are_nones.sum())
    return col


######################## RESPONSE TO OPEN QUESTION ########################

def clean_response_to_open_ended__inplace(col: np.array) -> np.array:
    return clean_character__inplace(col)


######################## CLEANER ########################

def clean_data__inplace(mtx: np.array, ordered_col_metadata: list) -> np.array:
    trans = mtx.transpose()
    for col, (col_name, col_type, cleaner) in zip(trans, ordered_col_metadata):
        try:
            cleaner(col)
        except Exception as e:
            print(f"There was an error processing column '{col_name}' of type '{col_type}'")
            raise e
    return trans.transpose()


######################## ENTRYPOINT ########################

def generate_cleaned_mtx(codebook_filepath: str, training_data_filepath: str, cleaned_data_filepath: str) -> np.array:

    # mapping each column to the cleaning function necessary for its type
    COLTYPE_TO_CLEANER = {
        'character [almost exclusively empty strings]': clean_character__inplace,
        'numeric': clean_numerical__inplace,
        'categorical': clean_categorical__inplace,
        'response to open-ended question': clean_response_to_open_ended__inplace,
        'date or time': clean_datetime__inplace,   
    }

    print(f"\nreading in codebook info from '{codebook_filepath}'")
    codebook_df = pd.read_csv(codebook_filepath, header=0)
    print("done")

    colname_to_type = {
        r["var_name"]: r["type_var"]
        for _, r in codebook_df.iterrows()
    }
    # we are going to be using a lot of memory, gonna clear useless stuff
    del codebook_df

    # pandas was giving me a ton of trouble trying to impute the types, and whatever NaN imputation
    # it did we clean immeidately anyway. Therefore just read everthing as string - not checking for NaN
    # as that is more performant and less of a headache
    print(f"reading in raw training data from '{training_data_filepath}'")
    training_data_df = pd.read_csv(training_data_filepath, header=0, dtype=str, na_filter=False)
    print("done")

    ordered_cols = training_data_df.columns.values
    training_data_np = training_data_df.to_numpy()
    del training_data_df

    ordered_col_metadata = [
        (col_name, colname_to_type[col_name], COLTYPE_TO_CLEANER[colname_to_type[col_name]])
        for col_name in ordered_cols
    ]
    print("cleaning data")
    cleaned_data = clean_data__inplace(training_data_np, ordered_col_metadata)
    print("done")

    trained_df = pd.DataFrame(cleaned_data, columns=ordered_cols)
    
    print(f"writing cleaned data to '{cleaned_data_filepath}'")
    trained_df.to_csv(cleaned_data_filepath, index=False)
    print("done")
    return cleaned_data


if __name__ == "__main__":
    # ideally create a CLI for this, can't be bothered to atm
    codebook_filepath, training_data_filepath, cleaned_data_filepath = sys.argv[1:]
    generate_cleaned_mtx(codebook_filepath, training_data_filepath, cleaned_data_filepath)
