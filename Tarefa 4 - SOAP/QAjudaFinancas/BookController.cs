using Microsoft.AspNetCore.Mvc;

[ApiController]
[Route("api/[controller]")]
public class BookController : ControllerBase
{
    private readonly IBookService _bookService;

    public BookController(IBookService bookService)
    {
        _bookService = bookService ?? throw new ArgumentNullException(nameof(bookService));
    }

    [HttpGet]
    [Route("GetBookInfo")]
    public ActionResult<string> GetBookInfo(int bookId)
    {
        var bookInfo = _bookService.GetBookInfo(bookId);
        return Content(bookInfo, "text/xml");
    }
}

