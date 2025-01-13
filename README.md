**FIRST: Installing Apache Airflow on Ubuntu 22.04**  

Step 1: Update system packages  
First, ensure your system is up-to-date:  

      sudo apt update && sudo apt upgrade -y  

Step 2: Install required dependencies  
Airflow requires python and pip. Check that you have them:  

    sudo apt install python3 python3-pip python3-venv -y  

Step 3: Create a virtual environment (Optional but recommended)  
This helps to isolate Airflow from the system’s Python packages:  

    python3 -m venv airflow_env  
    source airflow_env/bin/activate  
  
Step 4: Install Apache Airflow  
Set environment variables for Airflow installation:  

    export AIRFLOW_HOME=~/airflow  
    export PATH="$AIRFLOW_HOME/bin:$PATH"  
    
Install Airflow via pip:  

    pip install apache-airflow  
  
Step 5: Initialize the Airflow Database  
Airflow needs to initialize its metadata database:  

    airflow db init  
  
Step 6: Create an admin user  
Create an admin user to access the web interface:  
Example, what you maybe want to chance, at least email:   

    airflow users create \  
    --username admin \  
    --firstname Admin \  
    --lastname User \  
    --role Admin \  
    --email admin@example.com 		# At least you have to change your email  

When you run those, next it asks you need to choose password and write it again.   

Step 7: Start the Airflow web server and scheduler  
Start the webserver:  

    source airflow_env/bin/activate	# if there already reads (airflow_env), don’t do this!  
    airflow webserver --port 8080  
    
In a new terminal tab, start the scheduler:  

    source airflow_env/bin/activate	# if there already reads (airflow_env), don’t do this!  
    airflow scheduler  

Step 8: Access Airflow  
Open a browser and go to:  

    http://localhost:8080  
  
Log in with the admin credentials created earlier and you are ready to use Airflow.  
That's it!

**SECOND: ...** 
