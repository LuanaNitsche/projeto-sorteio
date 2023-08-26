import http.server
import socketserver
import random

PORT = 8000

class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith('.css'):
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            with open('styles.css', 'rb') as css_file:
                css_content = css_file.read()
                self.wfile.write(css_content)
        else:
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()

        alunos = [
                    'Ademir Batschauer Junior',
                    'Alex Sandro Rodrigues Mette',
                    'Ana Alice Rodrigues Do Nascimento',
                    'Angelo Miguel Requenha',
                    'Arthur Henrique Erhardt',
                    'Bernardo Martins Fontaina',
                    'Bianca Lanser Peres',
                    'Cristina Siewert Jansen',
                    'Daianna Marques Dos Santos',
                    'Daniel Nunes',
                    'Daniele Karine Modesto De Araujo',
                    'Fábio Henrique Peixe',
                    'Felipe Batista Dos Santos',
                    'Guilherme Bueno Zago',
                    'Isabela Caroline Reiter',
                    'Ivanir Stano',
                    'Júlia Francine De Oliveira',
                    'Luana Beatriz Nitsche',
                    'MARCO AURELIO RIBEIRO MARTINS',
                    'Matheus Santos Novak',
                    'Ryan Wessling Da Silva',
                    'Victor Gabriel',
                    'Victor Gomes Mendes',
                    'Victor Luís Zuchi',
                    'William Gonçalves Soares'
        ]

        shuffled_alunos = random.sample(alunos, len(alunos))  # Shuffle the list

        html = "<html><body><ul>"
        for i, aluno in enumerate(shuffled_alunos, start=1):
            html += f"<li>Lugar {i} - {aluno}</li>"
        html += "</ul></body></html>"

        self.wfile.write(html.encode())

with socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
