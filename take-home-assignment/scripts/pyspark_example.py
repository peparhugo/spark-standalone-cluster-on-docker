from pyspark.sql import SparkSession

spark = SparkSession.\
        builder.\
        appName("pyspark-notebook").\
        master("spark://spark-master:7077").\
        config("spark.executor.memory", "512m").\
        getOrCreate()
data = spark.read.csv(path="data/uk-macroeconomic-data.csv", sep=",", header=True)
unemployment = data.select(["Description", "Population (GB+NI)", "Unemployment rate"])
unemployment = unemployment.dropna()
unemployment = unemployment.\
               withColumnRenamed("Description", 'year').\
               withColumnRenamed("Population (GB+NI)", "population").\
               withColumnRenamed("Unemployment rate", "unemployment_rate")
unemployment.write.csv(path="take-home-assignment/data/uk-macroeconomic-unemployment-data.csv", sep=",", header=True, mode="overwrite")