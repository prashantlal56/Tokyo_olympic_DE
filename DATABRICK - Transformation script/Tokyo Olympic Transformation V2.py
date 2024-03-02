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

athelets = spark.read.format('csv').option('inferschema',True).option('header',True).load('dbfs:/mnt/tokyoolymic/raw-data/athelets.csv')
coaches = spark.read.format('csv').option('inferschema',True).option('header',True).load('dbfs:/mnt/tokyoolymic/raw-data/coaches.csv')
entriesgender = spark.read.format('csv').option('inferschema',True).option('header',True).load('dbfs:/mnt/tokyoolymic/raw-data/entriesgender.csv')
medals = spark.read.format('csv').option('inferschema',True).option('header',True).load('dbfs:/mnt/tokyoolymic/raw-data/medals.csv')
teams = spark.read.format('csv').option('inferschema',True).option('header',True).load('dbfs:/mnt/tokyoolymic/raw-data/teams.csv')

# COMMAND ----------

# MAGIC %md
# MAGIC ### Country Performance

# COMMAND ----------

country_base = athelets.groupBy('Country')\
    .agg(countDistinct(col('PersonName')).alias('player_cnt'),countDistinct(col('Discipline')).alias('discipline_participate'))

coaches_base = coaches.groupBy('Country').agg(countDistinct(col('Name')).alias('coaches_cnt'))

team_base = teams.groupBy('Country').agg(count(col('TeamName')).alias('team_cnt'))

medals = medals.withColumnRenamed('Team_Country','Country')

ccountry_performance = medals.join(country_base,'Country','left')\
                             .join(coaches_base,'Country','left')\
                             .join(team_base,'Country','left')\
                             .select(medals['*'],country_base['player_cnt'],country_base['discipline_participate']
                                     , coaches_base['coaches_cnt'], team_base['team_cnt'])

# COMMAND ----------

ccountry_performance.show()

# COMMAND ----------

ccountry_performance.write.format('csv').mode('overwrite').option('header',True).save('dbfs:/mnt/tokyoolymic/transformed-data/country_performance')

# COMMAND ----------


