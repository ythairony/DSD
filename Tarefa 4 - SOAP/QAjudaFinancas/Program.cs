var builder = WebApplication.CreateBuilder(args);

// Configuração do serviço MVC e adicionando controllers
builder.Services.AddControllers();

var app = builder.Build();

// Configuração do pipeline de execução
app.UseRouting();

app.UseEndpoints(endpoints =>
{
    endpoints.MapControllers(); // Isso mapeia os controllers do seu projeto
});

app.Run();
