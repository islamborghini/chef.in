<h1>Chef.in</h1>

<p>Chef.in is a Django-based web application designed to help users discover, share, and manage recipes in an intuitive and user-friendly interface. With Bootstrap CSS for styling, the platform offers a seamless experience for food enthusiasts to explore new dishes and organize their favorite recipes.</p>
<br>
<h2>Table of Contents</h2>

[Project Overview](#Project-Overview)<br>
[Motivation](#Motivation)<br>
[Getting Started](#Getting-Started)<br>
[Installation Prerequisites](#Installation-Prerequisites)<br>
[Running the Project Locally](#Running-the-Project-Locally)<br>
[Demo](#Demo)<br>
[Further Development and Contribution Guidelines](#Further-Development-and-Contribution-Guidelines)<br>
[Acknowledgements](#Acknowledgements)<br>
[Useful Resources](#Useful-Resources)<br>
[Contact](#Contact)<br>

<br>
<h2 id="Project-Overview">Project Overview </h2>

<p>Chef.in is a platform where users can explore a variety of recipes, add their own recipes, and manage their favorite ones. The application leverages Django for the backend and Bootstrap for a responsive, visually appealing frontend.</p>
<br><br>
<h2 id="Motivation">Motivation</h2>

<p>The motivation behind Chef.in is to create a community-driven space where food enthusiasts can easily find, share, and organize recipes. Whether you're a professional chef or a home cook, Chef.in aims to make recipe management straightforward and enjoyable.</p>
<br><br>
<h2 id="Getting-Started">Getting Started</h2>

<p>To get started with Chef.in, follow the steps below to set up the project locally on your machine.</p>
<br>
<h2 id="Installation-Prerequisites">Installation Prerequisites</h2>
<br>
<p>Ensure you have the following installed on your machine:</p>
<ul>
<li>Python 3.x</li>
<li>pip (Python package installer)</li>
</ul>
<h2 id="Running-the-Project-Locally">Running the Project Locally: </h2><br/>
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

<h2 id="Demo">Demo:</h2>
 
![image](https://github.com/islamborghini/chef.in/assets/82131413/5d78b578-6dbb-43d6-b9f2-0f9b37eaf79a) <br>
![image](https://github.com/islamborghini/chef.in/assets/82131413/9cef8c3f-728b-4f2e-be29-d0d4ccd49d46) <br>
![image](https://github.com/islamborghini/chef.in/assets/82131413/e89ce3ed-54a4-40b3-96c3-dddacd9eb35e) <br>
![image](https://github.com/islamborghini/chef.in/assets/82131413/1c118f64-bff8-444f-a859-fb13443b31c2) <br>
![image](https://github.com/islamborghini/chef.in/assets/82131413/1b150ff8-4dab-4db8-9efd-6613649e128d) <br>


<h2 id = "Further-Development-and-Contribution-Guidelines">Further Development and Contribution Guidelines</h2>

<p>We welcome contributions to improve Chef.in! To contribute:</p>
<ol>
<li>Fork the Project</li>
<li>Create your Feature Branch <code>git checkout -b feature/AmazingFeature</code></li>
<li>Commit your Changes  <code>git commit -m 'Add some AmazingFeature')</code></li>
<li>Push to the Branch  <code>git push origin feature/AmazingFeature)</code></li>
<li>Open a Pull Request</li>
<p>Please ensure your pull request adheres to the project's coding standards and includes relevant tests and documentation.</p>
</ol>

<h2  id = "Acknowledgements">Acknowledgements</h2>
<ul>
<li>Django - The web framework used for backend development.</li>
<li>Bootstrap - For the responsive and aesthetically pleasing frontend.</li>
<li>The open-source community for continuous inspiration and support.</li>
</ul>

<h2 id = "Useful-Resources">Useful Resources</h2>

[Django Documentation](https://docs.djangoproject.com/en/5.0/) <br>
[Bootstrap Documentation](https://getbootstrap.com/docs/4.1/getting-started/introduction/)<br>
<br>
<h2 id = "Contact">Contact</h2>

<p>Islam Assanov - islamassanov66@gmail.com </p>
<p>Project Link: https://github.com/islamborghini/chef.in</p>
