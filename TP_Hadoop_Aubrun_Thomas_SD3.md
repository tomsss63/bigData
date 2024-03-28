## __Par le terminal de commandes__
### Accéder au cluster via la commande ssh sur votre terminal préféré (Touches Windows+R puis taper cmd)
***-> Commande :***
```sh 
ssh maria_dev@localhost -p 2222
```
***-> Réponse :***
```sh
C:\Users\thoma>ssh maria_dev@localhost -p 2222
maria_dev@localhost's password:
Last login: Tue Mar 26 14:34:22 2024 from 172.18.0.3
[maria_dev@sandbox-hdp ~]$
```
> ***Remarque :*** La commande utilisée permet d'établir une connexion SSH (Secure Shell) à un hôte local (localhost) en utilisant le nom d'utilisateur & MDP maria_dev et en spécifiant le port 2222 pour cette connexion.
# 3. HDFS
## __3.1. Prise en main Commandes HDFS
***-> Commande :***
```sh
hdfs
```
***-> Réponse :***
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

> ***Remarque :*** ce que retourne cette commande est une liste de commandes liées à Hadoop Distributed File System (HDFS) 

> ***Remarque :*** hdfs -> (Système de fichiers distribués Hadoop) est un système de fichiers distribués dans hadoop c'est un tandem avec le systeme de mapreduce. Il utilise une architecture maître-esclave, où un NameNode (maître) gère le système de fichiers et les métadonnées, tandis que les DataNodes (esclaves) stockent les blocs de données réels. Il est optimisé pour le stockage de gros fichiers de données et est particulièrement adapté aux charges de travail analytiques et de traitement de données distribuées, telles que celles rencontrées dans l'analyse de données volumineuses (big data).

***-> Commande :***
```sh
hdfs dfs
``` 
***-> Réponse :***
```sh
Usage: hadoop fs [generic options]
        [-appendToFile <localsrc> ... <dst>]
        [-cat [-ignoreCrc] <src> ...]
        [-checksum <src> ...]
        [-chgrp [-R] GROUP PATH...]
        [-chmod [-R] <MODE[,MODE]... | OCTALMODE> PATH...]
        [-chown [-R] [OWNER][:[GROUP]] PATH...]
        [-copyFromLocal [-f] [-p] [-l] <localsrc> ... <dst>]
        [-copyToLocal [-p] [-ignoreCrc] [-crc] <src> ... <localdst>]
        [-count [-q] [-h] [-v] [-t [<storage type>]] [-u] <path> ...]
        [-cp [-f] [-p | -p[topax]] <src> ... <dst>]
        [-createSnapshot <snapshotDir> [<snapshotName>]]
        [-deleteSnapshot <snapshotDir> <snapshotName>]
        [-df [-h] [<path> ...]]
        [-du [-s] [-h] <path> ...]
        [-expunge]
        [-find <path> ... <expression> ...]
        [-get [-p] [-ignoreCrc] [-crc] <src> ... <localdst>]
        [-getfacl [-R] <path>]
        [-getfattr [-R] {-n name | -d} [-e en] <path>]
        [-getmerge [-nl] <src> <localdst>]
        [-help [cmd ...]]
        [-ls [-C] [-d] [-h] [-q] [-R] [-t] [-S] [-r] [-u] [<path> ...]]
        [-mkdir [-p] <path> ...]
        [-moveFromLocal <localsrc> ... <dst>]
        [-moveToLocal <src> <localdst>]
        [-mv <src> ... <dst>]
        [-put [-f] [-p] [-l] <localsrc> ... <dst>]
        [-renameSnapshot <snapshotDir> <oldName> <newName>]
        [-rm [-f] [-r|-R] [-skipTrash] [-safely] <src> ...]
        [-rmdir [--ignore-fail-on-non-empty] <dir> ...]
        [-setfacl [-R] [{-b|-k} {-m|-x <acl_spec>} <path>]|[--set <acl_spec> <path>]]
        [-setfattr {-n name [-v value] | -x name} <path>]
        [-setrep [-R] [-w] <rep> <path> ...]
        [-stat [format] <path> ...]
        [-tail [-f] <file>]
        [-test -[defsz] <path>]
        [-text [-ignoreCrc] <src> ...]
        [-touchz <path> ...]
        [-truncate [-w] <length> <path> ...]
        [-usage [cmd ...]]

Generic options supported are
-conf <configuration file>     specify an application configuration file
-D <property=value>            use value for given property
-fs <local|namenode:port>      specify a namenode
-jt <local|resourcemanager:port>    specify a ResourceManager
-files <comma separated list of files>    specify comma separated files to be copied to the map reduce cluster
-libjars <comma separated list of jars>    specify comma separated jar files to include in the classpath.
-archives <comma separated list of archives>    specify comma separated archives to be unarchived on the compute machines.

The general command line syntax is
bin/hadoop command [genericOptions] [commandOptions]
```

> ***Remarque :***  dfs est une commande qui inclue des opérations telles que la création de répertoires, la copie de fichiers vers et depuis le système de fichiers local, la suppression de fichiers, la modification des permissions et des propriétaires de fichiers, la gestion des instantanés, la récupération de métadonnées, etc.

### Pour connaitre la version de hadoop, la commande est : hadoop version (ou hdfs version)
#### 1. hadoop version 
***-> Commande :***
```sh
hadoop version
``` 
***-> Réponse :***
```sh
Hadoop 2.7.3.2.6.5.0-292
Subversion git@github.com:hortonworks/hadoop.git -r 3091053c59a62c82d82c9f778c48bde5ef0a89a1
Compiled by jenkins on 2018-05-11T07:53Z
Compiled with protoc 2.5.0
From source with checksum abed71da5bc89062f6f6711179f2058
This command was run using /usr/hdp/2.6.5.0-292/hadoop/hadoop-common-2.7.3.2.6.5.0-292.jar
```

#### 2. hdfs version
***-> Commande :***
```sh
hdfs version
```
***-> Réponse :***
```sh
Hadoop 2.7.3.2.6.5.0-292
Subversion git@github.com:hortonworks/hadoop.git -r 3091053c59a62c82d82c9f778c48bde5ef0a89a1
Compiled by jenkins on 2018-05-11T07:53Z
Compiled with protoc 2.5.0
From source with checksum abed71da5bc89062f6f6711179f2058
This command was run using /usr/hdp/2.6.5.0-292/hadoop/hadoop-common-2.7.3.2.6.5.0-292.jar
```

> ***Remarque :*** Les deux commandes malgrés leurs differences retournent le même résultat.

## 3.2. Importer et exporter des données
### hdfs dfs -ls : liste l'ensemble des fichiers du répertoire utilisateur HDFS.
***-> Commande :***
```sh
hdfs dfs -ls 
```
***-> Réponse :***
```sh
Found 1 items
drwx------   - maria_dev hdfs          0 2024-03-26 15:11 .Trash
```

### hdfs dfs -ls / : affiche ce qu’il y a à la racine HDFS.
***-> Commande :***
```sh
hdfs dfs -ls /
```
***-> Réponse :***
```sh
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
#### Quel est la commande pour lire le contenue de /user?
> ***Remarque :*** Pour faire cela, nous allons nous demander ce qui sort en réponse.  
***-> Commande :***
```sh
hdfs dfs -ls /user
```
***-> Réponse :***
```sh
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
```


### Que ce passe-il si vous refaite toute les commandes précedentes avec hadoop fs -- : hadoop fs -ls /

> ***Remarque :*** on se retrouve avec les mêmes résultats.

***-> Réponse :***
```sh 
Found 11 items
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

### Créez localement un fichier texte monfichier.txt, modifiez son contenu, sauvegardez et quittez

> ***Remarque :*** Ici on veut essayer de créer un fichier à partir de l'invit de commande. Pour cela on va utiliser la commande 'touch monfichier.txt' 


***-> Commande :***
```sh
touch monfichier.txt
```
> ***Remarque :*** En faisant ls, on remarque bien la création du fichier. 

***-> Réponse :***
```sh 
monfichier.txt  
```
> ***Remarque :*** La création du fichier s'étant bien faite, on va maintenant le modifier. 

***-> Commande :***
```sh
vi monfichier.txt
```
> ***Remarque :*** 
  - Pour passer en mode "insertion" -> i 
  - Pour sauvegarder vos changements et quitter, pressez Esc 
  - pour revenir au mode "normal", tapez :wq et appuyez sur Enter.

> ***Remarque :*** Ici pour vérifier si notre fichier a bien été modifié, on emploie la commande cat monfichier.txt

***-> Commande :***
```sh
cat monfichier.txt
```

***-> Réponse :***
```txt
Bonjour je m'appelle Thomas AUBRUN.
```

### Copiez ce fichier sur HDFS par hdfs dfs -put monfichier.txt. Utilisez hdfs dfs -ls -R pour vérifier.
> ***Remarque :*** On peut egalement utiliser hdfs dfs -copyFromLocal monfichier.txt

***-> Commande :***
```sh
hdfs dfs -ls -R
```
***-> Réponse :***
```sh
Found 1 items
-rw-r--r--   1 maria_dev hdfs         14 2024-03-25 16:16 monfichier.txt
```
> ***Remarque :*** Pour remplacer mon fichier si celui ci existe :  hdfs dfs -put -f monfichier.txt
Pour verifier si mon fichier est le bon : hdfs dfs -cat monfichier.txt

### Si vous voulez envoyer vos données vers HDFS sans garder une copie en local :
Cela doit se faire en 2 étapes. 
#### Etape 1 :

***-> Commande :***
```sh
hdfs dfs -copyFromLocal monfichier.txt
```
Etape 2: 

***-> Commande :***
```sh
rm monfichier.txt
```
> ***Remarque :*** ici on nous demande de confirmer l'action.

```
rm: remove regular file ‘monfichier.txt’? yes
```
## 3.3. Manipulation des données dans HDFS
### Affichez le contenu du fichier créer mais sur HDFS
> ***Remarque :*** Pour afficher le contenu, on se sert de la commande 'hdfs dfs -cat ...'
***-> Commande :***
```sh
hdfs dfs -cat monfichier.txt
```

### Supprimer un fichier depuis le système de fichiers HDFS :
***-> Commande :***
```sh
hdfs dfs -rm monfichier.txt
```
***-> Commande :***
```sh
hadoop fs -rm monfichier.txt
```

### Pour créer les répertoires du chemin 1 puis chemin2, … etc.
***-> Commande :***
```sh
hdfs dfs -mkdir CHEMIN1 CHEMIN2
```
> ***Remarque :*** Je souhaites vérifier

***-> Commande :***
```sh
hdfs dfs -ls
```
***-> Réponse :*** 
```sh
Found 3 items
drwx------   - maria_dev hdfs          0 2024-03-26 15:11 .Trash
drwxr-xr-x   - maria_dev hdfs          0 2024-03-26 15:14 CHEMIN1
drwxr-xr-x   - maria_dev hdfs          0 2024-03-26 15:14 CHEMIN2
```
### Créez localement un dossier nommé data et envoyez-le sur HDFS.
> ***Remarque :*** On veut créer le dossier data localement.

***-> Commande :***
```sh
mkdir data
```
> ***Remarque :*** On veut l'envoyer sur hdfs.

***-> Commande :***
```sh
hdfs dfs -put ./data /user/maria_dev/CHEMIN1
```
> ***Remarque :*** On vérifie si cela a bien fonctionné
```sh
hdfs dfs -ls /user/maria_dev/CHEMIN1
```

> ***Remarque :*** La fonction '-put' copie des fichiers du système local vers HDFS. Après la copie, le fichier existe à la fois sur le système local et dans HDFS.

### Copiez le fichier monfichier.txt dans le répertoire data à l’aide de la commande -cp (vérifiez).
***-> Commande :***
```sh
hdfs dfs -cp /user/maria_dev/monfichier.txt /user/maria_dev/CHEMIN1/data/monfichier.txt
```
***-> Commande :***
```sh
hdfs dfs -ls /user/maria_dev/CHEMIN1/data
```

***-> Réponse :*** 
```sh
Found 1 items
-rw-r--r--   1 maria_dev hdfs        347 2024-03-26 15:41 /user/maria_dev/CHEMIN1/data/monfichier.txt
```

> ***Remarque :*** La fonction '-cp' duplique des fichiers/répertoires au sein de HDFS. L'original reste inchangé à son emplacement, et une copie est créée dans un nouvel emplacement dans HDFS.

### Créez un dossier datasets dans le dossier data, puis déplacez monfichier.txt dans datasets à l’aide de la commande -mv, décrivez vos commandes.

> ***Remarque :*** On réutilise la même fonction '-mkdir' pour créer le chemin.

***-> Commande :***

``` sh
hdfs dfs -mkdir -p /user/maria_dev/CHEMIN1/data/datasets
```


> ***Remarque :*** Ci dessus nous voyons donc l'arborescence que nous créons: 

### -> Créer une copie de monfichier.txt dans le répertoire data sous le nom copiedemonfichier.txt.

> ***Remarque :*** Notre volonté est de déplacer le fichier 'monfichier.txt' dans datasets.

***-> Commande :***

```sh 
hdfs dfs -mv /user/maria_dev/CHEMIN1/data/monfichier.txt /user/maria_dev/CHEMIN1/data/datasets/monfichier.txt
```

> ***Remarque :*** La fonction '-mv' déplace des fichiers/répertoires au sein de HDFS. Après le déplacement, l'original n'existe plus à son emplacement initial.


### Créer une copie de monfichier.txt dans le répertoire data sous le nom copiedemonfichier.txt.
***-> Commande :***
```sh 
hdfs dfs -cp /user/maria_dev/CHEMIN1/data/datasets/monfichier.txt /user/maria_dev/CHEMIN1/data/copiedemonfichier.txt
```
### Avant de lancer cette commande, il faut vérifier que l’espace local disponible est suffisant pour recevoir les données HDFS, décrivez vos commandes.
***-> Commande :***
```sh 
df -h
```
***-> Réponse :*** 
```sh
Filesystem      Size  Used Avail Use% Mounted on
overlay         107G   28G   75G  27% /
tmpfs            64M     0   64M   0% /dev
/dev/sda3       107G   28G   75G  27% /etc/hosts
shm              64M   12K   64M   1% /dev/shm
tmpfs           5.4G   12M  5.4G   1% /run
tmpfs           1.1G     0  1.1G   0% /run/user/1001
tmpfs           1.1G     0  1.1G   0% /run/user/1002
tmpfs           1.1G     0  1.1G   0% /run/user/1005
tmpfs           1.1G     0  1.1G   0% /run/user/1020
tmpfs           1.1G     0  1.1G   0% /run/user/1023
tmpfs           1.1G     0  1.1G   0% /run/user/1000
tmpfs           1.1G     0  1.1G   0% /run/user/1003
tmpfs           1.1G     0  1.1G   0% /run/user/1004
tmpfs           1.1G     0  1.1G   0% /run/user/1008
tmpfs           1.1G     0  1.1G   0% /run/user/1026
tmpfs           1.1G     0  1.1G   0% /run/user/1012
tmpfs           1.1G     0  1.1G   0% /run/user/1010
tmpfs           1.1G     0  1.1G   0% /run/user/1011
tmpfs           1.1G     0  1.1G   0% /run/user/1015
```
> ***Remarque :*** En résumé, notre système a une bonne quantité d'espace disque libre disponible pour de futures données et applications.

### Si on veut supprimer un répertoire depuis le système de fichiers HDFS
***-> Commande :***
```sh 
hdfs dfs -rm -r /user/maria_dev/.... 
```
## 3.4 Manipulation de fichiers télécharger depuis un serveur
> ***Remarque :*** A partir de la VM, on veut télécharger les données disponibles sur le site : https://files.grouplens.org/datasets/movielens/ml-1m.zip pour cela on utilise la fonction 'wget'


***-> Commande :***
```sh
wget https://files.grouplens.org/datasets/movielens/ml-1m.zip
```
***-> Réponse :*** 
```sh
wget https://files.grouplens.org/datasets/movielens/ml-1m.zip
--2024-03-26 16:00:15--  https://files.grouplens.org/datasets/movielens/ml-1m.zip
Resolving files.grouplens.org (files.grouplens.org)... 128.101.65.152
Connecting to files.grouplens.org (files.grouplens.org)|128.101.65.152|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 5917549 (5.6M) [application/zip]
Saving to: ‘ml-1m.zip’

100%[=========================================================================================================================================>] 5,917,549   2.35MB/s   in 2.4s

2024-03-26 16:00:18 (2.35 MB/s) - ‘ml-1m.zip’ saved [5917549/5917549]
```
> ***Remarque :***  Validation de l'importation, Pas d'erreur liée à la sécurité 

### Décompressez le fichier zip
> ***Remarque :*** Le fichier rating.dat contient plus d’un million d’évaluations anonymes d'environ 3 900 films réalisé par 6 040 utilisateurs de MovieLens (voir le README pour plus de détails).

***-> Commande :***
```sh
unzip ml-1m.zip
```
***-> Réponse :*** 
```sh
Archive:  ml-1m.zip
```

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
>  ***Remarque :*** Ici on remarque que nous retrouvons en local le fichier datasets et l'intérieur de celui ci le fichier 'movies'

#### **Sur HDVS** 
***-> Commande :***
```sh 
hdfs dfs -mkdir -p /user/maria_dev/datasets/movies
```
>  ***Remarque :*** Ici il est possible de créer les deux répertoires en une seule ligne de commande. 

### Déroulez les étapes de création des deux dossier /datasets/movies et la copie du fichier rating.dat à partir du système local vers HDFS (dans movies).
### 1. Téléchargement du fichier 'ml_1m.zip' dans mon repertoire local datasets/movies
> ***Remarque :*** Etant donner que j'ai nettoyé mon dossier local j'ai de nouveaux téléchargé le ficher ml_1m.zip, mais cette fois ci directement dans mon fichier local datasets/movies 

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
Il est stocké dans un seul block "Total blocks (validated):      1 (avg. block size 24594131 B)". 

### Pour voir la décomposition d’un fichier en plusieurs blocs, récupérez le fichier zip MovieLens 25M Dataset.
> ***Remarque :*** On récupère le fichier qui se trouve à l'adresse suivante:
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


> ***Remarque :*** Le nombre 134217728 indique que la taille du bloc dans notre système de fichiers HDFS est de 134,217,728 octets, ce qui équivaut à 128 mégaoctets (MB).
Cette taille de bloc de 128 MB est la valeur par défaut pour les versions récentes de HDFS (Hadoop 2.x et ultérieures).


#### Vérifiez en envoyant un fichier sur HDFS et commenter votre analyse. (hint: Je vous demande de faire les manipulations pour voir le nombres des blocs)

### Vous pouvez changer la taille du bloc pour un fichier par la commande :

> ***Remarque :*** Pour cela je crée un nouveau répertoire dans hdfs

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

> ***Explication :*** Ce n'est pas possible de faire l'installation car nous sommes authentifiés en tant qu'utilisateur de maria_dev, nous n'avons donc pas les droits administrateur.
Il nous faut changer d'utilisateur vers le root. Pour cela la commande sudo su root vous bascule en root. Cela nous permettra par la suite d'installer différents packages.

***-> Commande :*** 
```sh
sudo su root
```



***-> Commande :*** 
```sh
yum install https://repo.ius.io/ius-release-el7.rpm https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
```

> ***Explication :***
Nous installons une mise à jour de la sandbox ci dessus afin de pouvoir installer des versions de python à jour par la suite.

### 4.1.2. Installation de python-pip:

```sh
yum install python-pip
```
> ***Explication :***
Nous installons python via cette commande

### 4.1.3. Instalation de de MrJob

``` sh
pip install pathlib
pip install mrjob==0.7.4
pip install PyYAML==5.4.1
```

> ***Explication :***
Via le code ci dessus, nous allons installer mrJob qui nous permettra par la suite de tester notre code python localement sans installer hadoop.

### 4.1.4 Installation de Nano

``` sh
yum install nano
```

> ***Explication :***
Nous installons ci dessus Nano qui est un éditeur de texte en ligne de commande, léger et facile à utiliser.


## 4.2. Execution du MapReduce en local

> ***Explication :***
Maintenant que nous avons téléchargé nano /  python / MrJob. Il est important de rebasculer sur maria_dev afin de poursuivre notre traitement.

```sh
su maria_dev
```


### 4.2.1. Récuperation du code et des données

```sh
wget https://github.com/juba-agoun/iut-hadoop/raw/main/filmEvaluation.py


wget https://github.com/juba-agoun/iut-hadoop/raw/main/evaluation.data
```

>***Remarque :***
La commande ci dessus nous permet de télécharger les données :
Le code python pour le map reduce : "filmEvaluation.py"
Les données : "evaluation.data"


```sh
python filmEvaluation.py evaluation.data
```


>***Remarque :***
Ce code nous permet de faire le map reduce sur les données evaluation.data
On applique notre fichier python a nos données évaluation. Cela permettra de compter le nombre d'occurences par note. 

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

> ***Remarque :***
Cette réponse nous indique que la note 4 a été attribuée 34174 fois, la note 5 21203 fois, la note 1 6111 fois, la note 2 11370 fois et la note 3 a été attribuée 27145 fois.


## 4.3. Execution du MapReduce sur Hadoop

```sh
hdfs dfs -put evaluation.data /user/maria_dev/CHEMIN1/data/evaluation.data
```

> ***Remarque :***
On met notre evaluation.data pour ranger nos fichiers afin trouver  le chemin du fichier evaluation.data. Cela nous permettra de l'intégrer dans le map reduce par la suite.

```sh
python filmEvaluation.py -r hadoop --hadoop-streaming-jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar hdfs:///user/maria_dev/CHEMIN1/data/evaluation.data
```

> ***Remarque :***
Avec l'aide de ce code nous avons pu éxécuter le mapreduce sur hadoop. Le code python une fois effectué nous a permis de compter les occurences des notes de chaque film. Nous observons que le mapreduce sur hadoop met + de temps à être éxécuté que localement. Ca s'explique par le fait que les moyens mis en oeuvre sur hadoop sont beaucoup trop importants compte tenu de la quantité de données à traiter. Localement, les moyens mis en oeuvre sont plus adaptés. A contrario, plus la quantité de données est importante, plus le mapreduce sur hadoop sera rentable en terme de temps.

# 5. Mise en pratique (Examen)

> ***Remarque :***
Pour pouvoir répondre aux prochaines problamatiques. Il va nous falloir récuperer le fichier tags.csv dans notre local. On va donc le transférer sur hadoop. Pour se faire nous utilisons la commande suivante :


***-> Commande :*** 
```sh
hdfs dfs -put /home/maria_dev/ml-25m/tags.csv /datasets/movies/ml-25m/
```


Et on vérifie que le fichier est bien dans hadoop avec la commande suivante :


```sh 
hdfs dfs -ls /datasets/movies/ml-25m 
``` 
> ***Remarque :***

Maitenant nous pouvons commencer à répondre aux questions :

## 5.1 Trouvez combien de tags chaque film possède ?

> ***Remarque :*** On créé le fichier tagsEvaluation afin de l'introduire dans un map reduce et le traiter avec notre code python.

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
> ***Remarque :***
Cette commande permet de créer un sample pour que l'on puisse tester sans avoir à utiliser tout le jeu de données :

***-> Commande :*** 
```sh
head -n 100 tags_full.csv > tags_sample_utilisateur.csv
```

> ***Remarque :*** Cette commande envoie le fichier dans hadoop :


***-> Commande :*** 

```sh
hdfs dfs -put tags_sample.csv hdfs:///datasets/movies/ml-25m/tags_sample.csv
```

> ***Remarque :*** On lance la commande pour tester le sample et enregistrer les résultats :



***-> Commande :*** 

```sh
python tagsEvaluation.py -r hadoop --hadoop-streaming-jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar hdfs:///datasets/movies/ml-25m/tags_sample.csv -o hdfs:///results/tags_output
```

> ***Remarque :*** On souhaite voir les résultats obtenus :

```sh
hdfs dfs -cat hdfs:///results/tags_output/part-00000
```


> ***RESULTAT :***
Voici les résultats obtenus : https://github.com/tomsss63/bigData/blob/33e7e146102f4800e5b4f110d12b2b43577d8f08/Q1_Sample/part-00000



> ***Remarque :***
Maitenant on essaie sur tout le jeu de données :


***-> Commande :*** 
```sh
python tagsEvaluation.py -r hadoop --hadoop-streaming-jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar hdfs:///datasets/movies/ml-25m/tags.csv -o hdfs:///results/tags_output_full
```
> ***Remarque :*** La même chose on souhaite voir les résultats obtenus mais sur l'ensemble des données :

***-> Commande :*** 
```sh
hdfs dfs -cat hdfs:///results/tags_output_full/part-00000
```

> ***RESULTAT :***
Voici les résultats obtenus: https://github.com/tomsss63/bigData/blob/33e7e146102f4800e5b4f110d12b2b43577d8f08/Q1/part-00000

## 5.2 

> ***Remarque :***
On créé le fichier film évaluation afin de l'introduire dans un map reduce et le traiter avec notre code python:


***-> Commande :*** 
```sh
vi tagsFilmEvaluation.py
```

> ***Remarque :***
Et on colle ce code. Ca va nous permettre de compter le nombre de tags associés à chaque film en utilisant un programme MapReduce :

```python
from mrjob.job import MRJob

class TagsParFilm(MRJob):

    def mapper(self, _, line):
        if line.startswith('movieId'):
            return
        parts = line.split(',')
        movieId = parts[1]
        yield movieId, 1

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    TagsParFilm.run()
```

> ***Remarque :***
On lance la commande pour tester sur le sample et enregistrer les résultats :


***-> Commande :*** 
```sh
python tagsFilmEvaluation.py -r hadoop --hadoop-streaming-jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar hdfs:///datasets/movies/ml-25m/tags_sample.csv -o hdfs:///results/tags_output_film
```

> ***Remarque :***
On verifie, avec une lecture.


***-> Commande :*** 
```sh
hdfs dfs -cat hdfs:///results/tags_output_film/part-00000
```


> ***RESULTAT :***
Voici les résultats obtenus : https://github.com/tomsss63/bigData/blob/33e7e146102f4800e5b4f110d12b2b43577d8f08/Q2_Sample/part-00000


> ***Remarque :***
Maitenant on essaie sur l'ensemble du jeu de données :


***-> Commande :*** 
```sh
python tagsFilmEvaluation.py -r hadoop --hadoop-streaming-jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar hdfs:///datasets/movies/ml-25m/tags.csv -o hdfs:///results/tags_output_film_full
```

***-> Commande :*** 
```sh
hdfs dfs -cat hdfs:///results/tags_output_film_full/part-00000
```


> ***RESULTAT :***
Voici les résultats obtenus: https://github.com/tomsss63/bigData/blob/33e7e146102f4800e5b4f110d12b2b43577d8f08/Q2/part-00000

## 5.3 


***-> Commande :*** 
```sh
hdfs fsck /datasets/movies/ml-25m/tags.csv -files -blocks
```

> ***Remarque :***
Voici le résultat pour la configuration 128 Mo :

***-> resultat :*** 
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

> ***Remarque :***
Pour la configuration en 64 Mo :


***-> Commande :*** 
```sh
hdfs dfs -D dfs.blocksize=64000000 -put tags.csv hdfs:///datasets/movies/ml-25m//tags_64.csv
```



## 5.4

> ***Remarque :***
On créé le fichier 

```sh
vi tagsQ4.py
```

> ***Remarque :***
Et on colle ce code. Ca va nous permettre de compter le nombre de fois que chaque tag est associé à chaque film en utilisant un programme MapReduce :


***-> Commande :*** 
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

> ***Remarque :***
On lance la commande pour tester sur le sample et enregistrer les résultats :


***-> Commande :*** 
```sh
python tagsQ4.py -r hadoop --hadoop-streaming-jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar hdfs:///datasets/movies/ml-25m/tags_sample.csv -o hdfs:///results/tags_output_Q4
```

> ***Remarque :***
Pour lire les résultats on fait :


***-> Commande :*** 
```sh
hdfs dfs -cat hdfs:///results/tags_output_Q4/part-00000
```


> ***RESULTAT :***
Voici les résultats obtenus : https://github.com/tomsss63/bigData/blob/33e7e146102f4800e5b4f110d12b2b43577d8f08/Q4_Sample/part-00000


> ***Remarque :***
Maitenant on essaie sur tout le jeu de données :


***-> Commande :*** 
```sh
python tagsQ4.py -r hadoop --hadoop-streaming-jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar hdfs:///datasets/movies/ml-25m/tags.csv -o hdfs:///results/tags_output_Q4_full
```


***-> Commande :*** 
```sh
hdfs dfs -cat hdfs:///results/tags_output_Q4_full/part-00000
```


> ***RESULTAT :***
Voici les résultats obtenus: https://github.com/tomsss63/bigData/blob/33e7e146102f4800e5b4f110d12b2b43577d8f08/Q4/part-00000