.. _quick-look:

Quick-Look
**********

What is a Data Profile?
~~~~~~~~~~~~~~~~~~~~~~~

In the case of this library, a data profile is a dictionary containing statistics and predictions about the underlying dataset. There are "global statistics" or `global_stats`, which contain dataset level data and there are "column/row level statistics" or `data_stats` (each column is a new key-value entry). 

The format for a profile is below:

.. code-block:: python

    "global_stats": {
        "samples_used": int,
        "column_count": int,
        "row_count": int,
        "row_has_null_ratio": float,
        "row_is_null_ratio": float,    
        "unique_row_ratio": float,
        "duplicate_row_count": int,
        "file_type": string,
        "encoding": string,
    },
    "data_stats": {
        <column name>: {
            "column_name": string,
            "data_type": string,
            "data_label": string,
            "categorical": bool,
            "order": string,
        "samples": list(str),
            "statistics": {
                "sample_size": int,
                "null_count": int,
                "null_types": list(string),
                "null_types_index": {
                    string: list(int)
                },
                "data_type_representation": string,
                "min": [null, float],
                "max": [null, float],
                "mean": float,
                "variance": float,
                "stddev": float,
                "histogram": { 
                    "bin_counts": list(int),
            "bin_edges": list(float),
                },
                "quantiles": {
                    int: float
                }
                "vocab": list(char),
                "avg_predictions": dict(float), 
                "data_label_representation": dict(float),
                "categories": list(str),
                "unique_count": int,
                "unique_ratio": float,
                "precision": {
                'min': int,
            'max': int,
            'mean': float,
            'var': float,
            'std': float,
            'sample_size': int,
            'margin_of_error': float,
            'confidence_level': float		
            },
                "times": dict(float),
                "format": string
            }
        }
    }

Support
~~~~~~~

Supported Data Formats
----------------------

* Any delimited file (CSV, TSV, etc.)
* JSON object
* Avro file
* Parquet file
* Pandas DataFrame

Data Types
----------

*Data Types* are determined at the column level for structured data

* Int
* Float
* String
* DateTime

Data Labels
-----------

*Data Labels* are determined per cell for structured data (column/row when the *profiler* is used) or at the character level for unstructured data.

* UNKNOWN
* ADDRESS
* BAN (bank account number, 10-18 digits)
* CREDIT_CARD
* EMAIL_ADDRESS
* UUID 
* HASH_OR_KEY (md5, sha1, sha256, random hash, etc.)
* IPV4
* IPV6
* MAC_ADDRESS
* PERSON
* PHONE_NUMBER
* SSN
* URL
* US_STATE
* DRIVERS_LICENSE
* DATE
* TIME
* DATETIME
* INTEGER
* FLOAT
* QUANTITY
* ORDINAL