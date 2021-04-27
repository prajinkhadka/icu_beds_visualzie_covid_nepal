# icu_beds_visualzie_covid_nepal

## Build docker image:
docker build -t covid-nepal-2021:v1 .

## Docker image 
docker run -p 8501:8501 covid-nepal-2021:v1

To deploy in a VM, 8501 port should be open, configure it from Network manager.


Dataset: - https://www.kaggle.com/akashsky13/nepal-icu-and-ventilators-occupancy-for-covid?fbclid=IwAR1JK9WjdvY9A096P0wEHzdndzwrTrdmKHZTYBZEStI65bbYIcPvp2yf6PY
