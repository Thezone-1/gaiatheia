# **Gaiatheia** 🌱  

**Gaiatheia** is a **machine learning benchmarking tool** that tracks **carbon emissions** using **CodeCarbon** and integrates with **Prometheus + Grafana** for real-time monitoring.

### **Features**  
- Tracks CO₂ emissions for ML models using `CodeCarbon`  
- Pushes emissions data to `Prometheus` via `Pushgateway`  
- Visualizes emissions in **Grafana** 

---
# **Setup** 
## **1️ Clone the Repository**  
First, clone the repository:  
```bash
git clone https://github.com/yourusername/gaiatheia.git
cd gaiatheia
```

---

## **2️ Install Dependencies**  
If you’re not using Docker, install the required Python dependencies:  
```bash
pip install -r requirements.txt
```
Ensure `CodeCarbon` is installed:  
```bash
pip install codecarbon
```

---

## **3️ Run the Machine Learning Models**  
Run the scripts to track the emissions. There are two ways to monitor the system:
- Export Data to CSV format
- Use Prometheus & Grafana to Track(currently in MVP phase) 

There are 3 simple experiments attached to it, you can run those or you can use the **Template.py** file and follow the instruction to build and run your own model.

### **Run Experiment 1**  
```bash
python experiment_1.py
```

---

## **4️ Setup Prometheus, Pushgateway, and Grafana with Docker**  
To track and visualize emissions, use **Docker Compose**:  

```bash
docker compose up
```

or if you are using podman 

```bash
podman compose up
```

This will start:  
- **Prometheus** (`http://localhost:9090`)  
- **Pushgateway** (`http://localhost:9091`)  
- **Grafana** (`http://localhost:3000`)  

---

## **5️ View Emissions in Grafana(Currently in MVP)**  
1. Open **Grafana**: `http://localhost:3000`  
2. Login with default credentials:  
   ```
   Username: admin  
   Password: admin
   ```
3. Add **Prometheus as a Data Source** (`http://prometheus:9090`)  
4. Import a new **dashboard** and use the metric:  
   ```
   codecarbon_emissions_kg
   ```

---
## **Contributing**  
Want to improve **Gaiatheia**? Feel free to open an **issue** or submit a **pull request**!  
