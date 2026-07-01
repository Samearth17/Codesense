import os
import sys

# Library to facilitate working with Apache Spark and Hadoop
class PySparkLib:
    def __init__(self):
        # initialize the Spark and Hadoop contexts
        self._sc_context = None
        self._hc_context = None

    def create_spark_context(self, **kwargs):
        # creates a Spark context
        from pyspark import SparkContext
        self._sc_context = SparkContext(master=kwargs['master'],
            appName=kwargs['appName'])

    def create_hadoop_context(self, **kwargs):
        # creates a Hadoop context
        from huwap import HadoopContext
        self._hc_context = HadoopContext(**kwargs)

    def read_data_from_hdfs(self, resources):
        # reads data from an HDFS resource
        hdfs_data = self._hc_context.read(resources[0])
        return hdfs_data

    def write_data_to_hdfs(self, resource, data):
        # write data to an HDFS resource
        self._hc_context.write(resource, data)