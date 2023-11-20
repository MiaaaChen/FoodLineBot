# FoodLineBot
It's a LINE Bot that provides users with information about nearby restaurants categorized by food type.


## Installation
```
pip install django  
pip install line-bot-sdk   
pip install requests  
pip install beautifulsoup4    
pip install pyshorteners  
```

## Usage
### Step 1. Create a provider in LINE Developers 
1. Get "Channel secret" and "Channel access token"
2. Put them in setting.py. 
   ![](https://imgur.com/1Z1zYCS.png)

### Step 2. Create a web service in Render
1. Link with Github and connect to Git repository.
   ![](https://imgur.com/zM3jzMD.png)
2. Type $ gunicorn mylinebot.wsgi:application in Start Command  
   ```
   gunicorn mylinebot.wsgi:application
   ```
 
   ![](https://imgur.com/d0QvEND.png)
4. Add two environment variables in Advanced Setting.  
   - LINE_CHANNEL_ACCESS_TOKEN  
   - LINE_CHANNEL_SECRET
   ![](https://imgur.com/e2ts7Jr.png)

### Step 3. Paste the service link to Django and LINE Developers
1. Add the link to "ALLOWED_HOST" in setting.py.
   ![](https://imgur.com/O3Y7zfm.png)
2. Paste the link to Webhook URL in LINE Developers.
   ![](https://imgur.com/PIMpXri.png)

### Step 4. Run the server and Deploy the service
1. Execute $ python manage.py runserver
   ```
   python3 manage.py sunserver
   ```
   ![](https://imgur.com/8JYEfgx.png)
2. Deploy web service
   ![](https://imgur.com/rnEJSsT.png)

### Step 5. Add FoodLineBot and Ask questions
Type 地區：XXX 類別：YYY  
We can get the search result on iFOODIE(愛食記)
![](https://imgur.com/xptC1M3.png)
