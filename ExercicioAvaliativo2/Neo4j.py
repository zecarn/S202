CREATE (:Pessoa:Trabalho{nome:'José Carlos', sexo:'M', idade:23, profissão:'Engenharia', especialidade:'Software', salário:6000.00}),
(:Pessoa:Trabalho{nome:'Laura Mc', sexo:'F', idade:23, profissâo:'Advogada', especialidade:'Direito Criminal', salário: 15000.00}),
(:Pessoa:Trabalho{nome:'Valéria Cristina', sexo:'F', idade:54, profissão:['Corretora','Gerente'], especilidade:'Seguros', salário:8000.00}),
(:Pessoa:Trabalho{nome:'Francisco Carlos', sexo:'M', idade:53, profissão:'Telecomunicações', especialidade:'Redes dos Computadores', salário:10000.00}),
(:Pessoa:Aposentado{nome:'Emílio', sexo:'M', idade:89, salário:5000.00}),(:Pessoa:Estudante{nome:'Miguel', sexo:'M', idade:20, grauDeEnsino:'Ensino Superior'}),
(:Pessoa:Estudante{nome:'Caio', sexo:'M', idade:12, grauDeEnsino:'Ensino Fundamental'}),
(:Pessoa:Estudante{nome:'Manuela', sexo:'F', idade:17, grauDeEnsino:'Ensino Médio'}),
(:Pet:Cachorro{nome:'Pateta',sexo:'M',idade:'4', raça:'Vira-lata', cor:['Preto','Branco','Cinza']}),
(:Pet:Cachorro{nome:'Lili', sexo:'F', idade:12, raça:'Pinsher', cor:['Preto','Marrom']}),
(:Pet:Passaro{nome:'Fred',sexo:'M',idade:2, raça:'Calopcita', cor:['Verde', 'Branco']})

MATCH (p:Pessoa{nome:'José Carlos'}),(pe:Pet{nome:'Pateta'}) CREATE (p)<-[:PET_DE{obtidoPor:'Adoção'}]-(pe)

MATCH (p1:Pessoa{nome:'Laura Mc'}),(pe1:Pet{nome:'Lili'}) CREATE (p1)<-[:PET_DE{obtidoPor:'Compra'}]-(pe1)

MATCH (p:Pessoa{nome:'Emílio'}),(a:Pet{nome:'Fred'}) CREATE (a)-[:PET_DE{obtidoPor:'Compra'}]->(p)

MATCH (p:Pessoa{nome:'Valéria Cristina'}), (p1:Pessoa{nome:'Francisco Carlos'}) CREATE (p1)-[:CASADO{anos:30}]->(p)

MATCH (p:Pessoa{nome:'Valéria Cristina'}), (p1:Pessoa{nome:'José Carlos'}) CREATE (p)-[:PAI_DE]->(p1)

MATCH (p:Pessoa{nome:'Francisco Carlos'}), (p1:Pessoa{nome:'José Carlos'}) CREATE (p)-[:PAI_DE]->(p1)

MATCH (p:Pessoa{nome:'Laura Mc'}), (p1:Pessoa{nome:'José Carlos'}) CREATE (p1)-[:CASADO{anos:2}]->(p)

MATCH (p:Pessoa{nome:'Emílio'}), (p1:Pessoa{nome:'Valéria Cristina'}) CREATE (p)-[:PAI_DE]->(p1)

MATCH (p:Pessoa{nome:'Manuela'}), (p1:Pessoa{nome:'Laura Mc'}) CREATE (p)-[:IRMAO_DE]->(p1)

MATCH (p:Pessoa{nome:'Caio'}), (p1:Pessoa{nome:'José Carlos'}) CREATE (p)-[:IRMAO_DE]->(p1)

MATCH (p:Pessoa{nome:'Miguel'}), (p1:Pessoa{nome:'José Carlos'}) CREATE (p)-[:IRMAO_DE]->(p1)
