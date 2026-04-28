from flask import render_template, url_for, request, redirect
from flask import current_app as app  # <--- THIS IS THE FIX
from . import db
from .models import Task

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        task_priority = request.form.get('priority', 'Medium')
        new_task = Task(content=task_content, priority=task_priority)
        
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'Issue adding task'
    
    status_filter = request.args.get('filter', 'all')
    
    if status_filter == 'completed':
        tasks = Task.query.filter_by(completed=True).all()
    elif status_filter == 'active':
        tasks = Task.query.filter_by(completed=False).all()
    else:
        tasks = Task.query.order_by(Task.completed, Task.date_created.desc()).all()
        
    pending_count = Task.query.filter_by(completed=False).count()
    
    return render_template('index.html', tasks=tasks, pending=pending_count, current_filter=status_filter)

@app.route('/update/<int:id>')
def update(id):
    task = Task.query.get_or_404(id)
    task.completed = not task.completed
    db.session.commit()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Task.query.get_or_404(id)
    db.session.delete(task_to_delete)
    db.session.commit()
    return redirect('/')

@app.route('/edit/<int:id>', methods=['POST'])
def edit(id):
    task = Task.query.get_or_404(id)
    task.content = request.form.get('content')
    db.session.commit()
    return redirect('/')