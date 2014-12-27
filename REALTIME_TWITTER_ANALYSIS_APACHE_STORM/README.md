# Real Time Twitter Analysis using Apache Storm

## About
The project helps to visualize the top N(=10) trending hash tags of Twitter in real time.   
[Apache Storm](https://storm.apache.org/) is used for real time stream processing while D3 for data visualization. A simple python server is used to host the webpage for visualization.

## Project Design

The project is designed by creating the storm topology consisting of a  

1. TweetSpout
2. ParseTweetBolt which is connected to tweet-spout using shuffleGrouping
3. CountBolt which is connected to tweet-spout using fieldsGrouping of tweet-word
4. IntermediateRankingsBolt and TotalRankingsBolt are open source Bolts availabe from [STORM](https://github.com/nathanmarz/storm-starter/tree/f5bdc720f50a0c46e90f0085c10217f2a6a3249f/src/jvm/main/storm/starter/bolt) github page used to collect and calculate the topN tweets ( N=10 in this case) 
5. ReportBolt connected to total-ranker using globalGrouping

The resulting Topology in code looks like below
```
    builder.setSpout("tweet-spout", tweetSpout, 1);
    builder.setBolt("parse-tweet-bolt", new ParseTweetBolt(), 10).shuffleGrouping("tweet-spout");
    builder.setBolt("count-bolt", new CountBolt(), 15).fieldsGrouping("parse-tweet-bolt", new Fields("tweet-word"));
    builder.setBolt("intermediate-ranker", new IntermediateRankingsBolt(TOP_N), 4).fieldsGrouping("count-bolt",new Fields("word"));
    builder.setBolt("total-ranker", new TotalRankingsBolt(TOP_N), 1).globalGrouping("intermediate-ranker");
    builder.setBolt("report-bolt", new ReportBolt(), 1).globalGrouping("total-ranker");
```


## Supporting programs  
1. [Redis](http://redis.io/)
2. [Flask](http://flask.pocoo.org/)
3. [D3](http://d3js.org/)
4. [Twitter4j](http://twitter4j.org/en/index.html)
5. [Storm](https://storm.apache.org/)

## Installation on Ubuntu
```
sudo apt-get install default-jdk -y  
sudo wget http://www.trieuvan.com/apache/incubator/storm/apache-storm-0.9.2-incubating/apache-storm-0.9.2-incubating.zip  
sudo unzip -o $(pwd)/apache-storm-0.9.2-incubating.zip   
sudo ln -s $(pwd)/apache-storm-0.9.2-incubating/ /usr/share/storm   
sudo ln -s /usr/share/storm/bin/storm /usr/bin/storm  
sudo wget https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein  
sudo mv lein /usr/bin  
sudo chmod 755 /usr/bin/lein  
sudo wget http://c758482.r82.cf2.rackcdn.com/sublime_text_3_build_3047.tar.bz2  
sudo tar vxjf Sublime\ Text\ 2.tar.bz2  
sudo mv Sublime\ Text\ 2 /opt/  
sudo ln -s /opt/Sublime\ Text\ 2/sublime_text /usr/bin/sublime   
sudo wget http://download-cf.jetbrains.com/idea/ideaIC-13.1.3.tar.gz   
sudo tar -xvzf ideaIC-13.1.3.tar.gz  
sudo apt-get install git-core -y  
sudo pip install redis  
sudo ufw disable  
sudo apt-get update -y  
sudo apt-get install maven -y  
sudo apt-get install vim -y  
sudo apt-get --yes install zookeeper zookeeperd -y  
sudo apt-get install redis-server -y  
sudo apt-get install python-software-properties -y  
sudo apt-get install python-pip -y  
sudo pip install flask  
sudo pip install redis  
```
### Storm installation
Follow the steps avaialable at (https://storm.apache.org/) for installation

## Running the project
### Start the flask server
```
python viz/app.py
```

### Package the project and feed it to storm
Update     "[Your customer key]",        "[Your secret key]",        "[Your access token]",        "[Your access secret]" inside the [TopNTweetTopology.java](https://github.com/bourneagain/DistributedSystems/blob/master/REALTIME_TWITTER_ANALYSIS_APACHE_STORM/src/jvm/udacity/storm/TopNTweetTopology.java) file
```
mvn package
storm jar <PATH_TO_JAR_WITH_DEPENDICIES.jar> <CLASS_TOPNTweetTopology>
```



### Project was developed as part of the [udacity](https://www.udacity.com/course/viewer#!/c-ud381/) online course.
