from infra.repository.filmesRepository import FilmesRepository

repositorio = FilmesRepository() 

'''Tá indo lá no repositório de filmes, que pega o DBConnection que está conecta ao banco'''

#repositorio.insert("Verônica", "Suspense", 2022)

#repositorio.delete("Verônica")

repositorio.update("Batman", 2022)

data = repositorio.select()

print(data)