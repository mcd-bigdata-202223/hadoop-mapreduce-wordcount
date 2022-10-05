# hadoop-mapreduce-wordcount

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
