# Reading a Parquet file into Pandas DataFrame from Google Storage with Apache Airflow
As of new version of pandas, read_parquet supports reading directly from Google Cloud Storage. Simply provide link to the bucket and Google Cloud Platform service account. 
last but not least, the package pyarrow and gcsfs need to install in your local machine.

how to install the package :
1. pip install pyarrow
2. pip install gcsfs
