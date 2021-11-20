from Banco import Banco


class UsuariosDB(object):

    def __init__(self, idusuario=0, nome="", cpf="", email="", usuario="", senha=""):
        self.info = {}
        self.idusuario = idusuario
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.usuario = usuario
        self.senha = senha
        self.imagens = []

    def insertUser(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("insert into usuarios (nome, cpf, email, " +
                      "usuario, senha) values ('" + self.nome + "', '" +
                      self.cpf + "', '" + self.email + "', '" +
                      self.usuario + "', '" + self.senha + "' )")

            banco.conexao.commit()
            c.close()

            return True
        except:
            return False

    def updateUser(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("update usuarios set nome = '" + self.nome + "'," +
                      "cpf = '" + self.cpf + "', email = '" + self.email +
                      "', usuario = '" + self.usuario + "', senha = '" + self.senha +
                      "' where idusuario = " + self.idusuario + " ")

            banco.conexao.commit()
            c.close()

            return "Usuário atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do usuário"

    def deleteUser(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("delete from usuarios where idusuario = " +
                      self.idusuario + " ")

            banco.conexao.commit()
            c.close()

            return "Usuário excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do usuário"

    def selectUser(self, idusuario):
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("select * from usuarios where idusuario = " +
                      idusuario + "  ")

            for linha in c:
                self.idusuario = linha[0]
                self.nome = linha[1]
                self.cpf = linha[2]
                self.email = linha[3]
                self.usuario = linha[4]
                self.senha = linha[5]

            c.close()

            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do usuário"

    def validarUsuarioSenha(self, usuario, senha):
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("select * from usuarios where usuario = '" +
                      usuario + "' and senha =  '"+senha+"' ")

            for linha in c:
                self.idusuario = linha[0]
                self.nome = linha[1]
                self.cpf = linha[2]
                self.email = linha[3]
                self.usuario = linha[4]
                self.senha = linha[5]

            c.close()

            return self.idusuario != 0
        except:
            return False

    def carregarImagens(self):
        banco = Banco()

        try:

            c = banco.conexao.cursor()

            c.execute(
                "select * from usuario_imagens where idusuario = " + str(self.idusuario))

            for linha in c:
                self.imagens.append([linha[0], linha[1], linha[2]])
            
            return self.imagens

        except Exception as e: 
            print(e)
            return self.imagens

    def salvarImagem(self, nome, caminho):
        banco = Banco()

        try:

            c = banco.conexao.cursor()

            c.execute("insert into usuario_imagens (idusuario, caminho) values (" +
                      str(self.idusuario) +", '"+ caminho +"' ) " )

            banco.conexao.commit()
            c.close()

            return True
        except Exception as e: 
            print(e)
            return False
