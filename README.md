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

chmod +x wordcount-*.py

mapred streaming -input /user/bigdata/wordcount/book.txt -output /user/bigdata/wordcount/output/ -mapper wordcount-mapper.py -reducer wordcount-reducer.py
```
Output the result:
```
hdfs dfs -cat /user/bigdata/wordcount/output/*


Stop the DFS:
```
stop-dfs.sh
```
