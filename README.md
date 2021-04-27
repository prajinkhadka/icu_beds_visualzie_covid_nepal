# icu_beds_visualzie_covid_nepal

## Build docker image:
docker build -t covid-nepal-2021:v1 .

## Docker image 
docker run -p 8501:8501 covid-nepal-2021:v1

To deploy in a VM, 8501 port should be open, configure it from Network manager.
