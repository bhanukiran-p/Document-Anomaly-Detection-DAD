# Backend Setup (FastAPI)

1. Navigate to the backend directory:
```
cd backend
```

2. Create a virtual environment:
```
python -m venv venv
```

3. Activate the virtual environment:
   - On Windows:
   ```
   venv\Scripts\activate
   ```
   - On macOS/Linux:
   ```
   source venv/bin/activate
   ```

4. Install dependencies:
```
pip install -r requirements.txt
```

5. Run the FastAPI server:
```
uvicorn main:app --reload
```

The backend server will start at `http://localhost:8000`
The swagger docs can be accessed at `http://localhost:8000/docs`