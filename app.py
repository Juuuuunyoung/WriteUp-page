from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/project/<string:project_id>')
def project_detail(project_id):
    # 여기서 프로젝트 ID를 사용하여 필요한 데이터를 로드할 수 있습니다.
    return render_template(f'project/{project_id}.html')

def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    # 예시 데이터를 넘겨줍니다.
    projects = [
        {
            'id': "Write-up",
            'title': 'test',
            'description': 'sub test',
            'image': 'images/logo.png'
        },
        {
            'id': "test",
            'title': '프로젝트 2',
            'description': '이것은 프로젝트 2의 설명입니다.',
            'image': 'images/project2.jpg'
        }
    ]
    return render_template('projects.html', projects=projects)


if __name__ == '__main__':
    app.run(debug=True)
