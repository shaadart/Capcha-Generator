body {
    font-family: Arial, sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: #f4f4f4;
    text-align: center;
    margin: 0;
}

.container {
    background: #fff;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    text-align: center;
    width: 300px;
}

img {
    border-radius: 5px;
    margin-bottom: 10px;
    border: 1px solid #ddd;
}

input[type="text"] {
    padding: 8px;
    font-size: 16px;
    width: 80%;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    text-align: center;
    outline: none;
}

.button-container {
    display: flex;
    justify-content: center;
    align-items: center;
}

button {
    padding: 10px 15px;
    border: none;
    background: #007bff;
    color: white;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;
    margin: 5px;
    transition: background 0.3s ease-in-out;
}

button:hover {
    background: #0056b3;
}

.refresh-icon {
    margin-left: 10px;
    cursor: pointer;
    font-size: 20px;
    transition: transform 0.3s ease-in-out;
}

.refresh-icon:hover {
    transform: rotate(180deg);
}
