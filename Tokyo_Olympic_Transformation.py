# Databricks notebook source
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import *

# COMMAND ----------

configs = {"fs.azure.account.auth.type": "OAuth",
"fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
"fs.azure.account.oauth2.client.id": "f3dfafd8-c4d9-4047-b20a-ff159cfaeb1a",
"fs.azure.account.oauth2.client.secret": "cXY8Q~Si6d~q0i6xiTbEEaQw0~wu49HnqsNvHa2z",
"fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/f50a35bc-a85f-4cd6-a0cf-1884b7e222ad/oauth2/token"}

dbutils.fs.mount(
source = "abfss://tokyo-olympic-data@tokyoolympicdatalal.dfs.core.windows.net", # contrainer@storageacc
mount_point = "/mnt/tokyoolymic",
extra_configs = configs)

# COMMAND ----------

# MAGIC %fs
# MAGIC
# MAGIC ls /mnt/tokyoolymic

# COMMAND ----------

spark

# COMMAND ----------

spark.sparkContext.getConf().getAll()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Creating Datafram for each data

# COMMAND ----------

# MAGIC %fs
# MAGIC
# MAGIC ls dbfs:/mnt/tokyoolymic/raw-data/

# COMMAND ----------

athelets = spark.read.format('csv').option('header',True).load('dbfs:/mnt/tokyoolymic/raw-data/athelets.csv')
coaches = spark.read.format('csv').option('header',True).load('dbfs:/mnt/tokyoolymic/raw-data/coaches.csv')
entriesgender = spark.read.format('csv').option('header',True).load('dbfs:/mnt/tokyoolymic/raw-data/entriesgender.csv')
medals = spark.read.format('csv').option('header',True).load('dbfs:/mnt/tokyoolymic/raw-data/medals.csv')
teams = spark.read.format('csv').option('header',True).load('dbfs:/mnt/tokyoolymic/raw-data/teams.csv')

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Athelets - Data Quality check

# COMMAND ----------

athelets.show(10, False)
athelets.printSchema()

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Coaches - Data Quality check

# COMMAND ----------

coaches.show(10, False)
coaches.printSchema()

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Entries Gender - Quality check

# COMMAND ----------

entriesgender.show(10, False)
entriesgender.printSchema()

# COMMAND ----------

for column in ['Female','Male','Total']:
    entriesgender = entriesgender.withColumn(f'{column}',col(f'{column}').cast(IntegerType()))
    print(f'Casted column : {column}')

# COMMAND ----------

entriesgender.printSchema()

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Medals - Data Quality Check

# COMMAND ----------

medals.show(10, False)
medals.printSchema()

# COMMAND ----------

for column in ['Rank', 'Gold', 'Silver', 'Bronze', 'Total', 'Rank by Total']:
    medals = medals.withColumn(f'{column}', col(f'{column}').cast(IntegerType()))
    print(f'Casted column : {column}')

# COMMAND ----------

medals.printSchema()

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Teams - Data Quality Check

# COMMAND ----------

teams.show(10, False)
teams.printSchema()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Storing Data : Transformed Data

# COMMAND ----------

athelets.write.format('csv').mode('overwrite').option('header',True).save('dbfs:/mnt/tokyoolymic/transformed-data/athelets')
coaches.write.format('csv').mode('overwrite').option('header',True).save('dbfs:/mnt/tokyoolymic/transformed-data/coaches')
medals.write.format('csv').mode('overwrite').option('header',True).save('dbfs:/mnt/tokyoolymic/transformed-data/medals')
entriesgender.write.format('csv').mode('overwrite').option('header',True).save('dbfs:/mnt/tokyoolymic/transformed-data/entriesgender')
teams.write.format('csv').mode('overwrite').option('header',True).save('dbfs:/mnt/tokyoolymic/transformed-data/teams')
