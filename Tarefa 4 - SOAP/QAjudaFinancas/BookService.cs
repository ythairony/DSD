using System.ServiceModel;

public interface IBookService
{
    string GetBookInfo(int bookId);
}

public class BookService : IBookService
{
    public string GetBookInfo(int bookId)
    {
        // Lógica para recuperar informações do livro com base no ID.
        return $"Informações sobre o Livro {bookId}: Título, Autor, Ano, etc.";
    }
}
