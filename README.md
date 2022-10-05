# hadoop-mapreduce-wordcount

Download the Lubuntu Virtual Machine with Hadoop Installed
https://myipleiria.sharepoint.com/:u:/s/BigData/EavonLJi881At7-5veEWg7gBkhidgJe4lwesfi_NruTDaQ?e=pXRLcG

Setup Distributed File System:
```
hdfs namenode -format
```

Start the DFS:
```
start-dfs.sh
```

Usage for "book.txt":

```
hdfs dfs -mkdir -p /user/bigdata/wordcount/
hdfs dfs -copyFromLocal book.txt /user/bigdata/wordcount/

pip install mrjob

python mrjob-wordcount.py -r hadoop hdfs:///user/bigdata/wordcount/book.txt  -o hdfs:///user/bigdata/wordcount/output

```
Output the result:
```
hdfs dfs -cat /user/bigdata/wordcount/output/*
```

Stop the DFS:
```
stop-dfs.sh
```
