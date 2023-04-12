# **Projet 10 python openclassrooms**

API sécurisée RESTful en utilisant Django REST

La version de **Python** à utiliser : _**3.10.5**_

# **ENVIRONNEMENT VIRTUEL**

Création de l'environnement virtuel :


Pour créer l'environnement virtuel il faut exécuter la commande suivante à la racine du projet :

    python -m venv env


Puis la commande suivante pour démarrer l'environnement :

-   sous Linux

    
    source env/bin/activate

-   sous Windows


    env/Scripts/activate.bat


Pour installer les packages spécifiés dans le fichier requirements.txt il faut exécuter la commande suivante :

    pip install -r requirements.txt


# **SCRIPT**

Il faut dans un premier temps, démarrer le serveur Django à l'aide de la commande suivante :

    python manage.py runserver

Pour accéder à l'API via le navigateur, il faut ouvrir l'url ___http://127.0.0.1:8000/login/___ dans un navigateur.

Il est cependant recommandé d'utiliser des outils plus ergonomique tel que Postman, afin d'utiliser des collections 
qui permettent d'avoir les appels deja construit et de n'avoir qu'à remplir les données à envoyer.

## Django administration

Pour accéder à l'interface d'administration de Django, il faut aller sur l'url  ___http://127.0.0.1:8000/admin/___ 

### Avec le fichier db.sqlite fournis

Compte admin:

| *Identifiant*   | *Mot de passe* |
|-----------------|----------------|
| admin@admin.fr  | Passw0rd!      |

Comptes utilisateurs:

| *Identifiant* | *Mot de passe* |
|---------------|----------------|
| test@test.fr  | 123456789!A    |
| test2@test.fr | 123456789!A    |
| test3@test.fr | 123456789!A    |


### Sans le fichier db.sqlite fournis

Il faut dans un premier temps générer la base de données avec la commande :

    python manage.py makemigrations

Puis, appliquer la migration à l'aide de la commande :

    python manage.py migrate

Pour créer un compte dans la partie administration, il faut exécuter la commande suivante et suivre les instructions :

    python manage.py createsuperuser

La création des comptes utilisateurs (contributeurs) se fait depuis l'appel API ___http://127.0.0.1:8000/signup/___

## Fonctionnalités de l'API

| *Point de terminaison d'API*                                              | *Méthode HTTP* | *URI*                                     |
|---------------------------------------------------------------------------|----------------|-------------------------------------------|
| Inscription de l'utilisateur                                              | POST           | /signup/                                  |
| Connexion de l'utilisateur                                                | POST           | /login/                                   |
| Récupérer la liste de tous les projets rattachés à l'utilisateur connecté | GET            | /projects/                                |
| Créer un projet                                                           | POST           | /projects/                                |
| Récupérer les détails d'un projet via son id                              | GET            | /projects/{id}/                           |
| Mettre à jour un projet                                                   | PUT            | /projects/{id}/                           |
| Supprimer un projet et ses problèmes                                      | DELETE         | /projects/{id}/                           |
| Ajouter un utilisateur (collaborateur) à un projet                        | POST           | /projects/{id}/users/                     |
| Récupérer la liste de tous les utilisateurs attachés à un projet          | GET            | /projects/{id}/users/                     |
| Supprimer un utilisateur d'un projet                                      | DELETE         | /projects/{id}/users/{id}/                |
| Récupérer la liste des problèmes liés à un projet                         | GET            | /projects/{id}/issues/                    |
| Créer un problème dans un projet                                          | POST           | /projects/{id}/issues/                    |
| Mettre à jour un problème dans un projet                                  | PUT            | /projects/{id}/issues/{id}/               |
| Supprimer un problème d'un projet                                         | DELETE         | /projects/{id}/issues/{id}/               |
| Créer des commentaires sur un problème                                    | POST           | /projects/{id}/issues/{id}/comments/      |
| Récupérer la liste de tous les commentaires liés à un problème            | GET            | /projects/{id}/issues/{id}/comments/      |
| Modifier un commentaire                                                   | PUT            | /projects/{id}/issues/{id}/comments/{id}/ |
| Supprimer un commentaire                                                  | DELETE         | /projects/{id}/issues/{id}/comments/{id}/ |
| Récupérer un commentaire via son id                                       | GET            | /projects/{id}/issues/{id}/comments/{id}/ |