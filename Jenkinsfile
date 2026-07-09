pipeline {
    agent any

    parameters {
        choice(
            name: '執行裝置',
            choices: ['android', 'web', 'both'],
            description: '選擇要執行的回歸測試'
        )
    }
    environment {
        PY = 'C:\\Users\\york_tu\\AppData\\Local\\Programs\\Python\\Python38\\python.exe'
        TESTDATA_APP = 'C:\\ProgramData\\Jenkins\\testdata\\app'
        TESTDATA_JIRA = 'C:\\ProgramData\\Jenkins\\testdata\\jira'
    }

    options {
        timestamps()
        disableConcurrentBuilds()
        timeout(time: 180, unit: 'MINUTES')
    }

    stages {
        stage('Copy Config') {
            steps {
                bat '''
                    cd /d "%WORKSPACE%"
                    if not exist "configs\\app" mkdir "configs\\app"
                    if not exist "jira\\config" mkdir "jira\\config"
                    xcopy /Y /I "%TESTDATA_APP%\\*" "configs\\app\\"
                    xcopy /Y /I "%TESTDATA_JIRA%\\*" "jira\\config\\"
                '''
            }
        }

        stage('Setup venv') {
            steps {
                bat '''
                    cd /d "%WORKSPACE%"
                    if not exist .venv (
                        "%PY%" -m venv .venv
                    )
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                    cd /d "%WORKSPACE%"
                    call .venv\\Scripts\\activate.bat
                    python -m pip install "jinja2<3.1"
                    python -m pip install -r requirements.txt
                '''
            }
        }

        stage('執行 Prod 股聊 Android端 回歸測試') {
            when { expression { params.RUN_TARGET in ['android', 'both'] } }
            steps {
                bat '''
                    cd /d "%WORKSPACE%"
                    call .venv\\Scripts\\activate.bat
                    python Project\\chat\\testsuite\\app\\gu\\android\\prod_regression.py
                '''
            }
        }

        stage('執行 Prod 股聊 Web端 回歸測試') {
            when { expression { params.RUN_TARGET in ['web', 'both'] } }
            steps {
                bat '''
                    cd /d "%WORKSPACE%"
                    call .venv\\Scripts\\activate.bat
                    python Project\\chat\\testsuite\\web\\gu\\prod_regression.py
                '''
            }
        }
    }

    post {
        always {
            bat '''
                cd /d "%WORKSPACE%"
                if exist "common\\Test-Reports" (
                    echo Test reports are under common\\Test-Reports
                )
            '''
            // 可選：封存報告
            // archiveArtifacts artifacts: 'common/Test-Reports/**/*', allowEmptyArchive: true
        }
        failure {
            echo 'Regression failed.'
        }
    }
}