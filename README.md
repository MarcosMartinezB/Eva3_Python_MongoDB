# Pokedex CLI - Python & MongoDB
## Evaluación Final Bases de Datos No Estructuradas

Este repositorio contiene el desarrollo de la evaluación integradora de la asignatura Bases de Datos No Estructuradas en INACAP. El proyecto consiste en el diseño e implementación de una aplicación de consola en Python conectada a una base de datos NoSQL en MongoDB, estructurada para gestionar una Pokedex completa mediante un entorno virtualizado.

## Contenido del Informe Académico y Proceso de Desarrollo

El documento técnico que acompaña este proyecto detalla paso a paso todo el trabajo realizado para cumplir con los objetivos de la evaluación:

### Selección y Virtualización del Entorno de Servidor

Se eligió e instaló Ubuntu Server 24.04.4 LTS como sistema operativo debido a su estabilidad, soporte a largo plazo (LTS) y total compatibilidad con el motor de base de datos.

El sistema operativo se ejecutó de forma virtualizada mediante VMware Workstation, creando un entorno seguro, independiente y aislado sin alterar el equipo principal.

### Instalación y Configuración de MongoDB

Se actualizó el sistema operativo y se instalaron las dependencias necesarias de red y seguridad (gnupg, curl).

Se incorporó la clave GPG oficial de MongoDB y se añadió el repositorio correspondiente a la versión 8.0 para sistemas Ubuntu.

Se instaló el gestor de base de datos junto con sus herramientas administrativas, verificando que el servicio quedara activo y en ejecución (`systemctl status mongod`).

### Arquitectura y Desarrollo del Software (Python y PyMongo)

#### Capa DAO (DAO.py)

Gestiona la conexión mediante el cliente de PyMongo (`mongodb://localhost:27017`), conectándose a la base de datos `PokemonDB` y a la colección `Pokemones`. Incluye métodos lógicos para registrar, modificar, eliminar y listar documentos.

#### Interfaz de Usuario y Menú (EVA3.py)

Programa interactivo basado en consola que presenta un menú con 11 opciones. Permite realizar operaciones CRUD y consultas avanzadas basadas en expresiones regulares (búsquedas exactas, por inicio, contenido o término de nombres) y filtros numéricos o de rangos sobre estadísticas base de los Pokémon (Vida, Ataque, Defensa, Velocidad).

### Pruebas y Evidencias

Se validó el funcionamiento del servidor mediante la consola interactiva `mongosh`, ejecutando comandos de verificación (`show dbs`, consultas a colecciones) para comprobar el almacenamiento correcto de los registros.

---

# Pokedex CLI - Python & MongoDB
## Final Evaluation Non-Structured Databases

This repository contains the development of the integrative evaluation for the Non-Structured Databases course at INACAP. The project consists of the design and implementation of a console application in Python connected to a NoSQL database in MongoDB, structured to manage a complete Pokedex within a virtualized environment.

## Academic Report Content and Development Process

The technical document accompanying this project details step-by-step all the work carried out to meet the evaluation objectives:

### Server Environment Selection and Virtualization

Ubuntu Server 24.04.4 LTS was selected and installed as the operating system due to its stability, long-term support (LTS), and full compatibility with the database engine.

The operating system was executed in a virtualized manner using VMware Workstation, creating a secure, independent, and isolated environment without altering the host machine.

### MongoDB Installation and Configuration

The operating system was updated, and necessary network and security dependencies (`gnupg`, `curl`) were installed.

The official MongoDB GPG key was imported, and the repository corresponding to version 8.0 for Ubuntu systems was added.

The database manager was installed along with its administrative tools, verifying that the service remained active and running (`systemctl status mongod`).

### Software Architecture and Development (Python and PyMongo)

#### DAO Layer (DAO.py)

Manages the connection using the PyMongo client (`mongodb://localhost:27017`), connecting to the `PokemonDB` database and the `Pokemones` collection. It includes logical methods to register, modify, delete, and list documents.

#### User Interface and Menu (EVA3.py)

Interactive console-based program featuring an 11-option menu. It allows CRUD operations and advanced queries based on regular expressions (exact searches, prefix, substring, or suffix matching) and numerical or range filters on base Pokémon statistics (HP, Attack, Defense, Speed).

### Testing and Evidence

Server functionality was validated using the interactive console `mongosh`, executing verification commands (`show dbs`, collection queries) to confirm correct record storage.
   