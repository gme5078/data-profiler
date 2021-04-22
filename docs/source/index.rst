.. _Data Profiler:

====================================
Data Profiler | What's in your data?
====================================

Purpose
=======

The DataProfiler is a Python library designed to make data analysis, monitoring and **sensitive data detection** easy.

Loading **Data** with a single command, the library automatically formats & loads files into a DataFrame. **Profiling** the Data, the library identifies the schema, statistics, entities and more. Data Profiles can then be used in downstream applications or reports.

The Data Profiler comes with a cutting edge pre-trained deep learning model, used to efficiently identify **sensitive data** (or **PII**). If customization is needed, it's easy to add new entities to the existing pre-trained model or insert a new pipeline for entity recognition.

The best part? Getting started only takes a few lines of code ([`Example CSV`_]):

.. code-block:: python

    import json
    from dataprofiler import Data, Profiler
    
    data = Data("your_file.csv") # Auto-Detect & Load: CSV, AVRO, Parquet, JSON, Text
    print(data.data.head(5)) # Access data directly via a compatible Pandas DataFrame
    
    profile = Profiler(data) # Calculate Statistics, Entity Recognition, etc
    readable_report = profile.report(report_options={"output_format":"pretty"})
    print(json.dumps(readable_report, indent=4))


To install the full package from pypi: 

.. code-block:: console

    pip install DataProfiler[ml]

If the ML requirements are too strict (say, you don't want to install tensorflow), you can install a slimmer package. The slimmer package disables the default sensitive data detection / entity recognition (labler)

Install from pypi: 

.. code-block:: console

    pip install DataProfiler

If you have suggestions or find a bug, [please open an `issue`_].

Visit the :ref:`Glossary<glossary>` to explore Data Profiler's terminology.

Components
==========

The Data Profiler is composed of three parts:

* A Data Reader that is used take in a wide range of inputs.
* A Profiler that provides a plethora of statistics on your data sets.
* And a Data Labeler to provide insight on the type of data being passed
  in.

To see each of these parts in action, visit the `Quick Look`_!


.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Getting Started:

   quick-look.rst
   install.rst
   profiling.rst
   data_readers.rst
   data_labeling.rst
   glossary.rst

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: User Guide:

   examples.rst
   faqs.rst

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Community:

   contributing.rst
   Changelog<https://github.com/capitalone/DataProfiler/releases>
   Feedback<https://github.com/capitalone/DataProfiler/issues/new/choose>
   GitHub<https://github.com/capitalone/DataProfiler>

.. _Quick Look: ./quick-look.html
.. _Example CSV: https://raw.githubusercontent.com/capitalone/DataProfiler/main/dataprofiler/tests/data/csv/aws_honeypot_marx_geo.csv
.. _issue: https://github.com/capitalone/DataProfiler/issues/new/choose

Versions
========
* `v0.4`_
* `v0.3`_

.. _v0.3: ../../v0.3/html/index.html
.. _v0.4: ../../v0.4/html/index.html

