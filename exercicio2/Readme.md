Engenharia de Software Moderna - Testes (Cap. 8)
Prof. Marco Tulio Valente
Aluno: Kayque Meira Siqueira

Exemplo bem simples de teste de um sistema de bibliotecas

O exemplo é apenas para fins didáticos. Particularmente, o sistema não possui interface com usuário ou banco de dados. E suas classes, em geral, possuem um subconjunto pequeno dos métodos e atributos de classes reais.

Biblioteca.py: classe que será testada
BibliotecaTest.py: teste da classe Biblioteca. Veja que os testes são bastante legíveis. Logo, você pode começar a entender o sistema por eles, antes de se esforçar para entender a implementação dos métodos na classe Biblioteca.
Atenção: O código inicialmente continha bugs propositalmente incluídos para falhar os casos de teste, mas eles foram resolvidos manualmente pelo aluno.

Para executar: 
    - Instale o pytest em seu sistema: pip install pytest.
    - Caminhe até a pasta do exercício (exercício 2).
    - Execute o comando "pytest BibliotecaTest.py" no terminal.
