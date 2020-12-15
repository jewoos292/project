FROM python:3.7.0

WORKDIR /home/

RUN git clone https://jewoos292:dnj8665xx!@github.com/jewoos292/project.git

WORKDIR /home/project/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN pip install gunicorn
RUN echo "SECRET_KEY=f4i%@0t59$uikiolja15an+chc^!_^(i96hkgtr8cdyjpd9l2t" > .env

RUN python manage.py migrate
RUN python manage.py collectstatic

EXPOSE 8000

CMD ["gunicorn","program.wsgi","--bind","0.0.0.0:8000"]
