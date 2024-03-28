## __Par le terminal de commandes__
### Accéder au cluster via la commande ssh sur votre terminal préféré (Touches Windows+R puis taper cmd)
***-> Commande :***
```sh 
ssh maria_dev@localhost -p 2222
```
***-> Réponse :***
```sh
C:\Users\vicol>ssh maria_dev@localhost -p 2222
maria_dev@localhost's password:
Last login: Tue Mar 26 14:34:22 2024 from 172.18.0.3
[maria_dev@sandbox-hdp ~]$
```
> ***Remarque :*** La commande utilisée permet d'établir une connexion SSH (Secure Shell) à un hôte local (localhost) en utilisant le nom d'utilisateur & MDP maria_dev et en spécifiant le port 2222 pour cette connexion.
# 3. HDFS
## __3.1. Prise en main Commandes HDFS__
-> commande : 
```sh
hdfs
```
retourn : 
```sh
where COMMAND is one of:
  dfs                  run a filesystem command on the file systems supported in Hadoop.
  classpath            prints the classpath
  namenode -format     format the DFS filesystem
  secondarynamenode    run the DFS secondary namenode
  namenode             run the DFS namenode
  journalnode          run the DFS journalnode
  zkfc                 run the ZK Failover Controller daemon
  datanode             run a DFS datanode
  dfsadmin             run a DFS admin client
  envvars              display computed Hadoop environment variables
  haadmin              run a DFS HA admin client
  fsck                 run a DFS filesystem checking utility
  balancer             run a cluster balancing utility
  jmxget               get JMX exported values from NameNode or DataNode.
  mover                run a utility to move block replicas across
                       storage types
  oiv                  apply the offline fsimage viewer to an fsimage
  oiv_legacy           apply the offline fsimage viewer to an legacy fsimage
  oev                  apply the offline edits viewer to an edits file
  fetchdt              fetch a delegation token from the NameNode
  getconf              get config values from configuration
  groups               get the groups which users belong to
  snapshotDiff         diff two snapshots of a directory or diff the
                       current directory contents with a snapshot
  lsSnapshottableDir   list all snapshottable dirs owned by the current user
                                                Use -help to see options
  portmap              run a portmap service
  nfs3                 run an NFS version 3 gateway
  cacheadmin           configure the HDFS cache
  crypto               configure HDFS encryption zones
  storagepolicies      list/get/set block storage policies
  version              print the version
  ```

### -> commande : dfs 
retourn : 
```command not found```

### difference ? 
Il y en a une qui marche et l'autre non... 

### -> Commande : hadoop version / hdfs version
-> hadoop version 
retourne : 
```
Hadoop 2.7.3.2.6.5.0-292
Subversion git@github.com:hortonworks/hadoop.git -r 3091053c59a62c82d82c9f778c48bde5ef0a89a1
Compiled by jenkins on 2018-05-11T07:53Z
Compiled with protoc 2.5.0
From source with checksum abed71da5bc89062f6f6711179f2058
This command was run using /usr/hdp/2.6.5.0-292/hadoop/hadoop-common-2.7.3.2.6.5.0-292.jar
```
-> hdfs version
retourne : 
```
Hadoop 2.7.3.2.6.5.0-292
Subversion git@github.com:hortonworks/hadoop.git -r 3091053c59a62c82d82c9f778c48bde5ef0a89a1
Compiled by jenkins on 2018-05-11T07:53Z
Compiled with protoc 2.5.0
From source with checksum abed71da5bc89062f6f6711179f2058
This command was run using /usr/hdp/2.6.5.0-292/hadoop/hadoop-common-2.7.3.2.6.5.0-292.jar
```

///// Quelle est la version hadoop de sandbox 2.6.5?

## 3.2. Importer et exporter des données
### -> Commande : hdfs dfs -ls 
Retourne : 
```Rien```

### -> 
Retourne : 
```
Found 11 items
drwxrwxrwx   - yarn   hadoop          0 2018-06-18 15:18 /app-logs
drwxr-xr-x   - hdfs   hdfs            0 2018-06-18 16:13 /apps
drwxr-xr-x   - yarn   hadoop          0 2018-06-18 14:52 /ats
drwxr-xr-x   - hdfs   hdfs            0 2018-06-18 14:52 /hdp
drwx------   - livy   hdfs            0 2018-06-18 15:11 /livy2-recovery
drwxr-xr-x   - mapred hdfs            0 2018-06-18 14:52 /mapred
drwxrwxrwx   - mapred hadoop          0 2018-06-18 14:52 /mr-history
drwxr-xr-x   - hdfs   hdfs            0 2018-06-18 15:59 /ranger
drwxrwxrwx   - spark  hadoop          0 2024-03-25 15:18 /spark2-history
drwxrwxrwx   - hdfs   hdfs            0 2018-06-18 16:06 /tmp
drwxr-xr-x   - hdfs   hdfs            0 2018-06-18 16:08 /user
```

### -> Commande : hdfs dfs -ls /user
Found 15 items
drwxr-xr-x   - admin     hdfs            0 2018-06-18 14:52 /user/admin
drwxrwx---   - ambari-qa hdfs            0 2018-06-18 14:52 /user/ambari-qa
drwxr-xr-x   - amy_ds    hdfs            0 2018-06-18 14:53 /user/amy_ds
drwxr-xr-x   - root      hdfs            0 2018-06-18 14:52 /user/anonymous
drwxr-xr-x   - druid     hadoop          0 2018-06-18 16:06 /user/druid
drwxr-xr-x   - hbase     hdfs            0 2018-06-18 15:08 /user/hbase
drwxr-xr-x   - hcat      hdfs            0 2018-06-18 15:12 /user/hcat
drwxr-xr-x   - hive      hdfs            0 2018-06-18 15:18 /user/hive
drwxrwxr-x   - livy      hdfs            0 2018-06-18 15:11 /user/livy
drwxr-xr-x   - maria_dev hdfs            0 2018-06-18 14:52 /user/maria_dev
drwxrwxr-x   - oozie     hdfs            0 2018-06-18 16:08 /user/oozie
drwxr-xr-x   - raj_ops   hdfs            0 2018-06-18 14:53 /user/raj_ops
drwxr-xr-x   - root      hdfs            0 2018-06-18 14:52 /user/root
drwxrwxr-x   - spark     hdfs            0 2018-06-18 15:10 /user/spark
drwxr-xr-x   - zeppelin  hdfs            0 2018-06-18 15:10 /user/zeppelin

### -> Que ce passe-il si vous refaite toute les commandes précedentes avec hadoop fs -- :        hadoop fs -ls /
Réponse : la meme chose 
Retourne : 
```Found 11 items
drwxrwxrwx   - yarn   hadoop          0 2018-06-18 15:18 /app-logs
drwxr-xr-x   - hdfs   hdfs            0 2018-06-18 16:13 /apps
drwxr-xr-x   - yarn   hadoop          0 2018-06-18 14:52 /ats
drwxr-xr-x   - hdfs   hdfs            0 2018-06-18 14:52 /hdp
drwx------   - livy   hdfs            0 2018-06-18 15:11 /livy2-recovery
drwxr-xr-x   - mapred hdfs            0 2018-06-18 14:52 /mapred
drwxrwxrwx   - mapred hadoop          0 2018-06-18 14:52 /mr-history
drwxr-xr-x   - hdfs   hdfs            0 2018-06-18 15:59 /ranger
drwxrwxrwx   - spark  hadoop          0 2024-03-25 15:55 /spark2-history
drwxrwxrwx   - hdfs   hdfs            0 2018-06-18 16:06 /tmp
drwxr-xr-x   - hdfs   hdfs            0 2018-06-18 16:08 /user
```

### -> Créez localement un fichier texte monfichier.txt, modifiez son contenu, sauvegardez et quittez
-> touch monfichier.txt pour créer un fichier vide nommé monfichier.txt

###### CREE : touch monfichier.txt
###### MODIFIER : vi monfichier.txt
Pour passer en mode "insertion" -> i 
Pour sauvegarder vos changements et quitter, pressez Esc 
pour revenir au mode "normal", puis tapez :wq et appuyez sur Enter.

###### Verifier : cat monfichier.txt
### -> Copiez ce fichier sur HDFS par hdfs dfs -put monfichier.txt. Utilisez hdfs dfs -ls -R pour vérifier.
On peut egalement utiliser hdfs dfs -copyFromLocal monfichier.txt
Réponse : 
```
Found 1 items
-rw-r--r--   1 maria_dev hdfs         14 2024-03-25 16:16 monfichier.txt
```
Pour remplacer mon fichier si celui ci existe :  hdfs dfs -put -f monfichier.txt
Pour verifier si mon fichier et le bon : hdfs dfs -cat monfichier.txt

### -> Si vous voulez envoyer vos données vers HDFS sans garder une copie en local :
Cela dois se faire en 2 etapes. 
Etape 1: 
hdfs dfs -copyFromLocal monfichier.txt

Etape 2: 
[maria_dev@sandbox-hdp ~]$ rm monfichier.txt
rm: remove regular file ‘monfichier.txt’? yes

## 3.3. Manipulation des données dans HDFS
### Affichez le contenu du fichier créer mais sur HDFS
hdfs dfs -cat ...
hdfs dfs -cat monfichier.txt

### -> Supprimer un fichier depuis le système de fichiers HDFS :
hdfs dfs -rm monfichier.txt
hadoop fs -rm monfichier.txt

### -> Pour créer les répertoires du chemin 1 puis chemin2, … etc.
[maria_dev@sandbox-hdp ~]$ hdfs dfs -mkdir CHEMIN1 CHEMIN2
[maria_dev@sandbox-hdp ~]$ hdfs dfs -ls
Found 3 items
drwx------   - maria_dev hdfs          0 2024-03-26 15:11 .Trash
drwxr-xr-x   - maria_dev hdfs          0 2024-03-26 15:14 CHEMIN1
drwxr-xr-x   - maria_dev hdfs          0 2024-03-26 15:14 CHEMIN2

### -> Créez localement un dossier nommé data et envoyez-le sur HDFS.
CREE -> mkdir data
ENVOIE -> hdfs dfs -put ./data /user/maria_dev/CHEMIN1
VERIFIER -> hdfs dfs -ls /user/maria_dev/CHEMIN1

### -> Copiez le fichier monfichier.txt dans le répertoire data à l’aide de la commande -cp (vérifiez).
[maria_dev@sandbox-hdp ~]$ hdfs dfs -cp /user/maria_dev/monfichier.txt /user/maria_dev/CHEMIN1/data/monfichier.txt
[maria_dev@sandbox-hdp ~]$ hdfs dfs -ls /user/maria_dev/CHEMIN1/data
Found 1 items
-rw-r--r--   1 maria_dev hdfs        347 2024-03-26 15:41 /user/maria_dev/CHEMIN1/data/monfichier.txt

### -> Créez un dossier datasets dans le dossier data, puis déplacez monfichier.txt dans datasets à l’aide de la commande -mv, décrivez vos commandes.
Dossier datasets à l'intérieur du dossier data qui se trouve dans CHEMIN1 :
-> hdfs dfs -mkdir -p /user/maria_dev/CHEMIN1/data/datasets
mkdir -> permet de crée un dossier 

### -> Créer une copie de monfichier.txt dans le répertoire data sous le nom copiedemonfichier.txt.
Déplacer monfichier.txt du dossier data vers datasets :*
-> hdfs dfs -mv /user/maria_dev/CHEMIN1/data/monfichier.txt /user/maria_dev/CHEMIN1/data/datasets/monfichier.txt
### -> Créer une copie de monfichier.txt dans le répertoire data sous le nom copiedemonfichier.txt.
-> hdfs dfs -cp /user/maria_dev/CHEMIN1/data/datasets/monfichier.txt /user/maria_dev/CHEMIN1/data/copiedemonfichier.txt

### -> Avant de lancer cette commande, il faut vérifier que l’espace local disponible est suffisant pour recevoir les données HDFS, décrivez vos commandes.
df -h

### -> Si on veut supprimer un répertoire depuis le système de fichiers HDFS
hdfs dfs -rm -r /user/maria_dev/.... 

## 3.4 Manipulation de fichiers télécharger depuis un serveur
A partir de la VM, téléchargez les données disponibles sur le site :
-> wget https://files.grouplens.org/datasets/movielens/ml-1m.zip
```
[maria_dev@sandbox-hdp ~]$ wget https://files.grouplens.org/datasets/movielens/ml-1m.zip
--2024-03-26 16:00:15--  https://files.grouplens.org/datasets/movielens/ml-1m.zip
Resolving files.grouplens.org (files.grouplens.org)... 128.101.65.152
Connecting to files.grouplens.org (files.grouplens.org)|128.101.65.152|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 5917549 (5.6M) [application/zip]
Saving to: ‘ml-1m.zip’

100%[=========================================================================================================================================>] 5,917,549   2.35MB/s   in 2.4s

2024-03-26 16:00:18 (2.35 MB/s) - ‘ml-1m.zip’ saved [5917549/5917549]
```
Pas d'erreur liée a la sécurité 

### Décompressez le fichier zip
Le fichier rating.dat contient plus d’un million d’évaluations anonymes d'environ 3 900 films réalisé par 6 040 utilisateurs de MovieLens (voir le README pour plus de détails).
[maria_dev@sandbox-hdp ~]$ unzip ml-1m.zip
Archive:  ml-1m.zip

### Créez un répértoire /datasets/movies en local et sur hdfs
#### **En local :** 
***-> Commande :***
```sh 
mkdir datasets
mkdir -p datasets/movies
```
***-> Réponse :***
1. Datasets
```sh
[maria_dev@sandbox-hdp ~]$ ls
data  datasets  ml-1m  ml-1m.zip  monfichier.txt  movies
```
2. movies 
```sh
[maria_dev@sandbox-hdp ~]$ ls datasets
movies
```
>  ***Remarque :*** Ici on remarque que nous retrouvons en local le fichier datasets et l'interrieur de celui ci le fichier movies

#### **Sur HDVS** 
***-> Commande :***
```sh 
hdfs dfs -mkdir -p /user/maria_dev/datasets/movies
```
>  ***Remarque :*** Ici il est possible de crée les deux répertoire en une seule ligne de commande. 

### Déroulez les étapes de création des deux dossier /datasets/movies et la copie du fichier rating.dat à partir du système local vers HDFS (dans movies).
### 1. Téléchargement du fichier 'ml_1m.zip' dans mon repertoire local datasets/movies
> ***Remarque :*** Etant donner que j'ai netoyer mon dossier local j'ai de nouveaux télécharger le ficher ml_1m.zip, mais cette fois si directement dans mon fichier local datasets/movies 

***-> Commande :***
```sh 
wget -P ~/datasets/movies https://files.grouplens.org/datasets/movielens/ml-1m.zip
```
***-> Réponse :***
```sh
[maria_dev@sandbox-hdp movies]$ ls ~/datasets/movies
ml-1m.zip
```
### 2. Dézipage du fichier 'ml_1m.zip'

> ***Remarque :*** Une fois cela fait je dézipe le fichier

***-> Commande :***
```sh 
unzip /home/maria_dev/datasets/movies/ml-1m.zip -d /home/maria_dev/datasets/movies/
```
***-> Réponse :***
```sh
Archive:  /home/maria_dev/datasets/movies/ml-1m.zip
   creating: /home/maria_dev/datasets/movies/ml-1m/
  inflating: /home/maria_dev/datasets/movies/ml-1m/movies.dat
  inflating: /home/maria_dev/datasets/movies/ml-1m/ratings.dat
  inflating: /home/maria_dev/datasets/movies/ml-1m/README
  inflating: /home/maria_dev/datasets/movies/ml-1m/users.dat
```
### 3. copie du fichier rating.dat à partir du système local 'datasets/movies' vers HDFS (dans movies).

***-> Commande :***
```sh 
hdfs dfs -put /home/maria_dev/datasets/movies/ml-1m/ratings.dat /user/maria_dev/datasets/movies/
```
***-> Réponse :***
> Vérification : 'hdfs dfs -ls /user/maria_dev/datasets/movies/'

```sh
Found 1 items
-rw-r--r--   1 maria_dev hdfs   24594131 2024-03-27 14:34 /user/maria_dev/datasets/movies/ratings.dat
```

### 4. Affichez combien de blocs occupe le fichier avec la commande hdfs fsck [chemin vers votre fichier] -files -blocks (Commentez!)

***-> Commande :***
```sh 
hdfs fsck /user/maria_dev/datasets/movies/ratings.dat -files -blocks
```
***-> Réponse :***

> ***Remarque :*** Nombre de Blocs : HDFS divise les fichiers en blocs (par défaut, la taille d'un bloc est de 128 MB sur HDFS 2.x et plus) pour une distribution et un stockage efficaces sur le cluster. fsck nous montre combien de blocs sont utilisés pour stocker ratings.dat. Si le fichier est grand, il sera divisé en plusieurs blocs.

```sh
Connecting to namenode via http://sandbox-hdp.hortonworks.com:50070/fsck?ugi=maria_dev&files=1&blocks=1&path=%2Fuser%2Fmaria_dev%2Fdatasets%2Fmovies%2Fratings.dat
FSCK started by maria_dev (auth:SIMPLE) from /172.18.0.2 for path /user/maria_dev/datasets/movies/ratings.dat at Wed Mar 27 14:37:05 UTC 2024
/user/maria_dev/datasets/movies/ratings.dat 24594131 bytes, 1 block(s):  OK
0. BP-243674277-172.17.0.2-1529333510191:blk_1073743070_2255 len=24594131 repl=1

Status: HEALTHY
 Total size:    24594131 B
 Total dirs:    0
 Total files:   1
 Total symlinks:                0
 Total blocks (validated):      1 (avg. block size 24594131 B)
 Minimally replicated blocks:   1 (100.0 %)
 Over-replicated blocks:        0 (0.0 %)
 Under-replicated blocks:       0 (0.0 %)
 Mis-replicated blocks:         0 (0.0 %)
 Default replication factor:    1
 Average block replication:     1.0
 Corrupt blocks:                0
 Missing replicas:              0 (0.0 %)
 Number of data-nodes:          1
 Number of racks:               1
FSCK ended at Wed Mar 27 14:37:05 UTC 2024 in 8 milliseconds
```

> ***Remarque :*** 
Le fichier fait 24,594,131 octets, soit environ 23.45 MB.
Il est stocker dans un seul block "Total blocks (validated):      1 (avg. block size 24594131 B)". 

### Pour voir la décomposition d’un fichier en plusieurs blocs, récupérez le fichier zip MovieLens 25M Dataset.

Récuperez le fichiers qui se trouve:
https://files.grouplens.org/datasets/movielens/ml-25m.zip

#### 1. Télechargement

***-> Commande :*** 

```sh 
wget https://files.grouplens.org/datasets/movielens/ml-25m.zip
```

***-> Réponse :***

```sh
--2024-03-27 14:51:28--  https://files.grouplens.org/datasets/movielens/ml-25m.zip
Resolving files.grouplens.org (files.grouplens.org)... 128.101.65.152, 64:ff9b::8065:4198
Connecting to files.grouplens.org (files.grouplens.org)|128.101.65.152|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 261978986 (250M) [application/zip]
Saving to: ‘ml-25m.zip’

100%[=============================================>] 261,978,986 6.06MB/s   in 2m 30s

2024-03-27 14:54:00 (1.67 MB/s) - ‘ml-25m.zip’ saved [261978986/261978986]
```
#### 2. Dézipage


***-> Commande :*** 

```sh 
unzip ml-25m.zip
```

***-> Réponse :***

```sh
Archive:  ml-25m.zip
   creating: ml-25m/
  inflating: ml-25m/tags.csv
  inflating: ml-25m/links.csv
  inflating: ml-25m/README.txt
  inflating: ml-25m/ratings.csv
  inflating: ml-25m/genome-tags.csv
  inflating: ml-25m/genome-scores.csv
  inflating: ml-25m/movies.csv
```
#### 3. création d'un nouveaux fichier et copie 

***-> Commande :*** 

```sh 
hdfs dfs -mkdir -p /datasets/movies/ml-25m
```
```sh 
hdfs dfs -put /home/maria_dev/ml-25m/ratings.csv /datasets/movies/ml-25m/
```
```sh 
hdfs fsck /user/maria_dev/datasets/movies/ml-25m/ratings.dat -files -blocks
```
***-> Réponse :***

```sh
Status: HEALTHY
 Total size:    678260987 B
 Total dirs:    0
 Total files:   1
 Total symlinks:                0
 Total blocks (validated):      6 (avg. block size 113043497 B)
 Minimally replicated blocks:   6 (100.0 %)
 Over-replicated blocks:        0 (0.0 %)
 Under-replicated blocks:       0 (0.0 %)
 Mis-replicated blocks:         0 (0.0 %)
 Default replication factor:    1
 Average block replication:     1.0
 Corrupt blocks:                0
 Missing replicas:              0 (0.0 %)
 Number of data-nodes:          1
 Number of racks:               1
FSCK ended at Wed Mar 27 15:21:23 UTC 2024 in 123 milliseconds
```
> ***Remarque :*** Le fichier fait 678,260,987 octets
Il est stocker dans 6 block "Total blocks (validated):   Total blocks (validated):      6 (avg. block size 113043497 B)


## 3.5. Fichiers de configuration HDFS

### Consultez le contenu de ce fichier.
#### Quelle est la valeur du paramètre dfs.replication. Ce dernier permet de préciser le nombre de réplication d'un block sur les noeuds d’un cluster. Justifiez !

***-> Commande :*** 

```sh
cat /etc/hadoop/conf/hdfs-site.xml
```

***-> Réponse :***

```JSON
    <property>
      <name>dfs.replication</name>
      <value>1</value>
    </property>
```

> ***Remarque :*** Nous voyons ci dessus que la valeur de replication est de "1". Les données ne sont stockées qu'en un seul exemplaire, ce qui peut être risqué en termes de perte de données.


#### Quelle est la taille du bloc sur votre HDFS ?

***-> Commande :*** 
```sh
hdfs getconf -confKey dfs.blocksize
```

***-> Réponse :***

134217728


> ***Remarque :*** Le nombre 134217728 indique que chaque fichier stocké dans HDFS sera découpé en blocs de 128 MB pour le stockage sur le cluster.


#### Vérifiez en envoyant un fichier sur HDFS et commenter votre analyse. (hint: Je vous demande de faire les manipulations pour voir le nombres des blocs)

```sh
hdfs dfs -mkdir -p /chemin/hdfs/cible/
```

```sh
echo "Exemple" > exemple.txt
```

```sh
hdfs dfs -D dfs.blocksize=67108864 -put exemple.txt /chemin/hdfs/cible/exemple.txt
```

> ***Remarque :*** Cette commande nous permet de passer le fichier "exemple.txt" en version 64 BIT.

# 4 . Hadoop

## 4.1. Préparation de la vm (MrJob, Python ...)

### 4.1.1. Mise à jour de la SandBox HDP

```
sudo su root
```

> ***Explication :***
Pour installer les packages ci dessous, nous devons passer par root, n'ayant pas les accès admistrateur sur maria_dev



```
yum-config-manager --save --setopt=HDP-SOLR-2.6-100.skip_if_unavailable=true

yum install https://repo.ius.io/ius-release-el7.rpm https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
```

> ***Explication :***
Nous installons une mise à jour de la sandbox ci dessus afin de pouvoir installer des versions de python à jour par la suite.

### 4.1.2. Installation de python-pip:

```
yum install python-pip
```
> ***Explication :***
Nous installons python via cette commande

### 4.1.3. Instalation de de MrJob

```
pip install pathlib
pip install mrjob==0.7.4
pip install PyYAML==5.4.1
```

> ***Explication :***
Via le code ci dessus, nous allons installer mrJob qui nous permettra par la suite de tester notre code python localement sans installer hadoop.

### 4.1.4 Installation de Nano

```
yum install nano
```

> ***Explication :***
Nous installons ci dessus Nano quiun éditeur de texte en ligne de commande, léger et facile à utiliser.


## 4.2. Execution du MapReduce en local

Nous repassons sur maria_dev afin de poursuivre notre traitement.

```
su maria_dev
```

### 4.2.1. Récuperation du code et des données

```
wget https://github.com/juba-agoun/iut-hadoop/raw/main/filmEvaluation.py


wget https://github.com/juba-agoun/iut-hadoop/raw/main/evaluation.data
```

La commande ci dessus nous permet de télécharger les données :
Le code python pour le map reduce : "filmEvaluation.py"
Les données : "evaluation.data"


```
python filmEvaluation.py evaluation.data
```


Ce code nous permet de faire le map reduce sur les données evaluation.data

```sh
[maria_dev@sandbox-hdp ~]$ python filmEvaluation.py evaluation.data
No configs found; falling back on auto-configuration
No configs specified for inline runner
Creating temp directory /tmp/filmEvaluation.maria_dev.20240326.203304.849415
Running step 1 of 1...
job output is in /tmp/filmEvaluation.maria_dev.20240326.203304.849415/output
Streaming final output from /tmp/filmEvaluation.maria_dev.20240326.203304.849415/output...
"4"     34174
"5"     21203
"1"     6111
"2"     11370
"3"     27145
Removing temp directory /tmp/filmEvaluation.maria_dev.20240326.203304.849415...
```


Cette réponse nous indique que la note 4 a été attribuée 34174 fois, la note 5 21203 fois, la note 1 6111 fois, la note 2 11370 fois et la note 3 a été attribuée 27145 fois.


## 4.3. Execution du MapReduce sur Hadoop

```
hdfs dfs -put evaluation.data /user/maria_dev/CHEMIN1/data/evaluation.data
```

Nous changeons le chemin pour trouver le fichier evaluation.data afin de l'intégrer dans le map reducing par la suite.

```sh
python filmEvaluation.py -r hadoop --hadoop-streaming-jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar hdfs:///user/maria_dev/CHEMIN1/data/evaluation.data
```

Ce code nous permet d'executer le mapreduce sur hadoop. Le code python permet de compter les occurences des notes de chaque film. Nous observons que le mapreduce sur hadoop met + de temps à être éxécuté que localement. Ca s'explique par le fait que les moyens mis en oeuvre sur hadoop sont beaucoup trop importants compte tenu de la quantité de données à traiter. Localement, les moyens mis en oeuvre sont plus adaptés.

# 5. Mise en pratique (Examen)

> ***Explication :***
Avant de commencer la manipulation du fichier tags.csv il faut le transférer sur hadoop. Pour se faire nous utilisons la commande suivante :

```sh
hdfs dfs -put /home/maria_dev/ml-25m/tags.csv /datasets/movies/ml-25m/
```

Et on vérifie que le fichier est bien dans hadoop avec la commande suivante :


```sh 
hdfs dfs -ls /datasets/movies/ml-25m 
``` 


Maitenant nous pouvons commencer à répondre aux questions :

## 5.1 Trouvez combien de tags chaque film possède ?

On créé le fichier 

```sh
vi tagsEvaluation.py
```

Et on colle ce code. Ca va nous permettre de compter le nombre de tags introduits par chaque utilisateur en utilisant un programme MapReduce :

```python
from mrjob.job import MRJob

class TagsParUtilisateur(MRJob):

    def mapper(self, _, line):
        if line.startswith('userId'):
            return
        parts = line.split(',')
        userId = parts[0]
        yield userId, 1

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    TagsParUtilisateur.run()

```

Cette commande permet de créer un sample pour que l'on puisse tester sans avoir à utiliser tout le jeu de données :

```sh
head -n 100 tags_full.csv > tags_sample_utilisateur.csv
```

Cette commande envoie le fichier dans hadoop :

```sh
hdfs dfs -put tags_sample.csv hdfs:///datasets/movies/ml-25m/tags_sample.csv
```


On lance la commande pour tester le sample et enregistrer les résultats :

```sh
python tagsEvaluation.py -r hadoop --hadoop-streaming-jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar hdfs:///datasets/movies/ml-25m/tags_sample.csv -o hdfs:///results/tags_output
```

Voici les résultats obtenus :

```sh
hdfs dfs -cat hdfs:///results/tags_output/part-00000
```

Voici les résultats obtenus : https://github.com/tomsss63/bigData/blob/33e7e146102f4800e5b4f110d12b2b43577d8f08/Q1_Sample/part-00000

Maitenant on essaie sur tout le jeu de données :

```sh
python tagsEvaluation.py -r hadoop --hadoop-streaming-jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar hdfs:///datasets/movies/ml-25m/tags.csv -o hdfs:///results/tags_output_full
```

```sh
hdfs dfs -cat hdfs:///results/tags_output_full/part-00000
```

Voici les résultats obtenus: https://github.com/tomsss63/bigData/blob/33e7e146102f4800e5b4f110d12b2b43577d8f08/Q1/part-00000

## 5.2 

On créé le fichier 

```sh
vi tagsFilmEvaluation.py
```

Et on colle ce code. Ca va nous permettre de compter le nombre de tags associés à chaque film en utilisant un programme MapReduce :

```python
from mrjob.job import MRJob

class TagsParFilm(MRJob):

    def mapper(self, _, line):
        if line.startswith('userId'):
            return
        parts = line.split(',')
        movieId = parts[1]
        yield movieId, 1

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    TagsParFilm.run()
```

On lance la commande pour tester sur le sample et enregistrer les résultats :

```sh
python tagsFilmEvaluation.py -r hadoop --hadoop-streaming-jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar hdfs:///datasets/movies/ml-25m/tags_sample.csv -o hdfs:///results/tags_output_film
```

Pour lire les résultats on fait :

```sh
hdfs dfs -cat hdfs:///results/tags_output_film/part-00000
```

Voici les résultats obtenus : https://github.com/tomsss63/bigData/blob/33e7e146102f4800e5b4f110d12b2b43577d8f08/Q2_Sample/part-00000

Maitenant on essaie sur tout le jeu de données :

```sh
python tagsFilmEvaluation.py -r hadoop --hadoop-streaming-jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar hdfs:///datasets/movies/ml-25m/tags.csv -o hdfs:///results/tags_output_film_full
```

```sh
hdfs dfs -cat hdfs:///results/tags_output_film_full/part-00000
```

Voici les résultats obtenus: https://github.com/tomsss63/bigData/blob/33e7e146102f4800e5b4f110d12b2b43577d8f08/Q2/part-00000

## 5.3 

```sh
hdfs fsck /datasets/movies/ml-25m/tags.csv -files -blocks
```

Voici le résultat pour la configuration 128 Mo :

```sh
Connecting to namenode via http://sandbox-hdp.hortonworks.com:50070/fsck?ugi=maria_dev&files=1&blocks=1&path=%2Fdatasets%2Fmovies%2Fml-25m%2Ftags.csv
FSCK started by maria_dev (auth:SIMPLE) from /172.18.0.2 for path /datasets/movies/ml-25m/tags.csv at Wed Mar 27 01:19:32 UTC 2024
/datasets/movies/ml-25m/tags.csv 38810332 bytes, 1 block(s):  OK
0. BP-243674277-172.17.0.2-1529333510191:blk_1073743077_2259 len=38810332 repl=1

Status: HEALTHY
 Total size:    38810332 B
 Total dirs:    0
 Total files:   1
 Total symlinks:                0
 Total blocks (validated):      1 (avg. block size 38810332 B)
 Minimally replicated blocks:   1 (100.0 %)
 Over-replicated blocks:        0 (0.0 %)
 Under-replicated blocks:       0 (0.0 %)
 Mis-replicated blocks:         0 (0.0 %)
 Default replication factor:    1
 Average block replication:     1.0
 Corrupt blocks:                0
 Missing replicas:              0 (0.0 %)
 Number of data-nodes:          1
 Number of racks:               1
FSCK ended at Wed Mar 27 01:19:32 UTC 2024 in 2 milliseconds


The filesystem under path '/datasets/movies/ml-25m/tags.csv' is HEALTHY
```

Pour la configuration en 64 Mo :
```sh
hdfs dfs -D dfs.blocksize=64000000 -put tags.csv hdfs:///datasets/movies/ml-25m//tags_64.csv
```



## 5.4

On créé le fichier 

```sh
vi tagsQ4.py
```

Et on colle ce code. Ca va nous permettre de compter le nombre de fois que chaque tag est associé à chaque film en utilisant un programme MapReduce :

```python
from mrjob.job import MRJob
import csv

class TagCount(MRJob):

    def mapper(self, _, line):
        # Parsing CSV line
        row = next(csv.reader([line]))
        if len(row) >= 3:
            movie_id = row[1]
            tag = row[2]
            yield (movie_id, tag), 1

    def reducer(self, key, values):
        movie_id, tag = key
        yield movie_id, (tag, sum(values))

if __name__ == '__main__':
    TagCount.run()

```

On lance la commande pour tester sur le sample et enregistrer les résultats :

```sh
python tagsQ4.py -r hadoop --hadoop-streaming-jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar hdfs:///datasets/movies/ml-25m/tags_sample.csv -o hdfs:///results/tags_output_Q4
```

Pour lire les résultats on fait :

```sh
hdfs dfs -cat hdfs:///results/tags_output_Q4/part-00000
```

Voici les résultats obtenus : https://github.com/tomsss63/bigData/blob/33e7e146102f4800e5b4f110d12b2b43577d8f08/Q4_Sample/part-00000

Maitenant on essaie sur tout le jeu de données :

```sh
python tagsQ4.py -r hadoop --hadoop-streaming-jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar hdfs:///datasets/movies/ml-25m/tags.csv -o hdfs:///results/tags_output_Q4_full
```

```sh
hdfs dfs -cat hdfs:///results/tags_output_Q4_full/part-00000
```

Voici les résultats obtenus: https://github.com/tomsss63/bigData/blob/33e7e146102f4800e5b4f110d12b2b43577d8f08/Q4/part-00000