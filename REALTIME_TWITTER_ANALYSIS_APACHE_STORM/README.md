

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
