<h1>How to install Chef.In from the GitHub Repository: </h1><br/>
<ol>
<li>Navigate to the desired directory on your machine.
<li>Clone the project using the command below:
<br/>
<code>git clone https://github.com/islamborghini/chef.in.git</code></br>
</li>
<li>
Navigate into the Project Directory:
<br/>
<code>cd chef-in</code>
</li>
<h3>Create and Activate a Virtual Environment:</h3>
<li>
Create a virtual environment: <br/>
<code>python -m venv env</code>
</li>
<li>Activate the virtual environment:<br/>
On Windows:<br/>
<code>.\env\Scripts\activate</code> <br/>
On macOS/Linux: <br/>
<code>source env/bin/activate</code></li>
<h3>Install the Project Dependencies:</h3>
<li>Ensure you have the latest version of pip: <br>
<code>pip install --upgrade pip</code>
</li>
<li>Install all dependencies: <br/>
<code>pip install -r requirements.txt</code>
</li>
<li>
Apply Database Migrations:
Run the following commands to apply migrations and set up the database:<br/>
<code>python manage.py makemigrations<br/>
 python manage.py migrate</code>
</li>
<h3>
Create a superuser to access the Django admin interface:</h3>  
<code> python manage.py createsuperuser</code>
<li>
Follow the prompts to set up a username, email, and password.
</li>
<h3>Run the Development Server:</h3>
<li>Start the Django development server:<br/>
<code>python manage.py runserver</code></li>
<li>Visit http://127.0.0.1:8000 in your web browser to see the project running locally.</li>
</ol><br>
Troubleshooting Tips:<br>
If you encounter errors related to dependencies, try updating them or reinstalling with:<br/>
<code>pip install --force-reinstall -r requirements.txt</code>
<br>
<h1>Development process insights:</h1><br/>
<h3>I chose to develop the project based on the criteria given on the Notion page:</h3>
<ol>
  <li>**Уровень 1:**

- Создание базового веб-макета, который включает в себя главную страницу с рецептами <br>
![image](https://github.com/islamborghini/chef.in/assets/82131413/5d78b578-6dbb-43d6-b9f2-0f9b37eaf79a) <br>
![image](https://github.com/islamborghini/chef.in/assets/82131413/9cef8c3f-728b-4f2e-be29-d0d4ccd49d46) <br>

</li>
 <li>**Уровень 2:**

- Разработка страницы детального просмотра рецепта, на которой отображается информация
   ![image](https://github.com/islamborghini/chef.in/assets/82131413/e89ce3ed-54a4-40b3-96c3-dddacd9eb35e)

- Реализация функции поиска, которая позволяет пользователю находить рецепты по названию.
  ![image](https://github.com/islamborghini/chef.in/assets/82131413/1c118f64-bff8-444f-a859-fb13443b31c2)

</li>

<li>
**Уровень 3:**

- Используйте любой API на ваш выбор либо же по данной [ссылке](https://developer.edamam.com/edamam-docs-recipe-api)
![image](https://github.com/islamborghini/chef.in/assets/82131413/1b150ff8-4dab-4db8-9efd-6613649e128d)


  I used <a href="https://developer.edamam.com/edamam-nutrition-api">EDAMAM Nutrition Analysis API</a> to calculate proteins, fat, and carbohydrates based on the given ingredients.  
</li>
</ol>
<br>
<br>
<h1>Compromises in the development and weaknesses of the project </h1>
<h2>Compromises:</h2>
<ol>
  <li>
  <h3>Feature Set vs. Development Timeline</h3>
  <p>I had to find the balance between the number of features that can be included into the project and the time that I was given for the development (3 days).</p>
  </li>
  <li>
  <h3>Performance vs. Aesthetics
</h3>
  <p>I had to choose between an attractive appeal from the site and the functionality, so I chose the latter one since they better show my development skills.</p>
  </li>
</ol>
<h2>Weaknesses:</h2>
<ol>
  <li>The project crashes if you add an ingredient without a quantity. It gets no response from EDAMAM API, so the server denies to work.</li>
  <li>The pictures on the recipy description sites are not scaled for other devices (than my Macbook).</li>
  <li>The categories are hard-coded instead of taking them from the database. This might lead to inconsistencies when adding a new category. </li>
</ol>
