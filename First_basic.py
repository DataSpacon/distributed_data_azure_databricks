# Databricks notebook source

spark.databricks.chauffeur.enableIdleContextTracking


# COMMAND ----------

print(spark.conf.get("spark.databricks.clusterUsageTags.sparkVersion"))

# COMMAND ----------

spark.version

# COMMAND ----------

# MAGIC %sh
# MAGIC ls

# COMMAND ----------

# MAGIC %md
# MAGIC ### Using %conda allows us to save, reuse or share an environment.

# COMMAND ----------

# MAGIC %conda env export -f /dbfs/sub_dir/my_env.yml

# COMMAND ----------

# MAGIC %md
# MAGIC Import back

# COMMAND ----------

# MAGIC %conda env update -f /dbfs/sub_dir/my_env.yml

# COMMAND ----------

# MAGIC %md
# MAGIC #### Libraries
# MAGIC We cannot uninstall any libraries included in the Databricks Runtime or any installed at cluster level.

# COMMAND ----------

# MAGIC %pip install pandas==2.1
# MAGIC # Wheel package - we need to rename it first to keep it consistenth with a naming convention
# MAGIC # (importing to dbfs, removes special characters)
# MAGIC %pip install /dbfs/mypackage-0,0,1-py3-none-any.whl
# MAGIC %pip install /path/to/my_package.whl
# MAGIC # to uninstall, it is necessary to pass the -y option to say yes as default, because there is no keyboard input when running this option
# MAGIC %pip uninstall -y pandas
# MAGIC # Requirements file
# MAGIC 
# MAGIC %pip freeze > /dbfs/sub_dir/requirements.txt
# MAGIC %pip install  -r /dbfs/sub_dir/requirements.txt
