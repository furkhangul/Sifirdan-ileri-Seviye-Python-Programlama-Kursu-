"""
Bu dersimizde ise selenium kütüphanesi ile kullanılan selectorsleri nerden bulabileceğimizi
nasıl kullanabileceğimizi, nelere yarayacağını anlattım.
"""

"""
Öncelikle html ve css birleşimi olarak ders anlatıldı bu birleşim sonucu
hocamızın veridği contentler üzerinden selectorlari anlamamız sağlanıyor.
"""


"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kurslar</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f9;
        }
        #header {
            text-align: center;
            background: #007bff;
            color: white;
            padding: 20px;
        }
        #container {
            padding: 20px;
        }
        .course {
            background: white;
            border: 1px solid #ddd;
            margin-bottom: 20px;
            padding: 15px;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }
        .course h2 {
            color: #007bff;
        }
        .course p {
            margin: 10px 0;
        }
        .course button {
            padding: 10px 15px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .course button:hover {
            background-color: #0056b3;
        }
        #form-section {
            margin-top: 30px;
            background: white;
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }
        #form-section h3 {
            margin-bottom: 20px;
            color: #007bff;
        }
        #form-section form {
            display: flex;
            flex-direction: column;
        }
        #form-section form input,
        #form-section form textarea,
        #form-section form button {
            margin-bottom: 15px;
            padding: 10px;
            font-size: 16px;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
        #form-section form button {
            background-color: #28a745;
            color: white;
            cursor: pointer;
        }
        #form-section form button:hover {
            background-color: #218838;
        }
    </style>
</head>
<body>

    <h1 id="header">Kurslar</h1>

    <div id="container">
        <div class="course python">
            <h2>Python Kursu</h2>
            <p>Python programlamaya giriş yapın ve bu popüler dili öğrenin.</p>
            <button>Daha Fazla Bilgi</button>
        </div>

        <div class="course angular">
            <h2>Angular Kursu</h2>
            <p>Modern web uygulamaları geliştirmek için Angular'ı öğrenin.</p>
            <button>Daha Fazla Bilgi</button>
        </div>

        <div class="course javascript">
            <h2>JavaScript Kursu</h2>
            <p>Web sitelerinize etkileşim katmak için JavaScript öğrenin.</p>
            <button>Daha Fazla Bilgi</button>
        </div>
    </div>

    <div id="form-section">
        <h3>Bizimle İletişime Geçin</h3>
        <form action="#" method="POST">
            <label for="name">Adınız:</label>
            <input type="text" id="name" name="name" placeholder="Adınızı girin" required>
            
            <label for="email">E-posta:</label>
            <input type="email" id="email" name="email" placeholder="E-posta adresinizi girin" required>
            
            <label for="message">Mesajınız:</label>
            <textarea id="message" name="message" rows="5" placeholder="Mesajınızı buraya yazın" required></textarea>
            
            <button type="submit">Gönder</button>
        </form>
    </div>

</body>
</html>
"""
