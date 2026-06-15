{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "11909212-3938-4500-9e57-ae53491d6145",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Importações\n",
    "import pandas as pd\n",
    "import ast\n",
    "import unicodedata\n",
    "import matplotlib.pyplot as plt\n",
    "import matplotlib.ticker as mt\n",
    "from sklearn.linear_model import LinearRegression\n",
    "from sklearn.metrics import r2_score\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "57492ff5-80d4-4a62-8896-6d5e0eac9b32",
   "metadata": {},
   "outputs": [],
   "source": [
    "\"\"\"Dados json\n",
    "Nesta etapa estou carregando os dados json\"\"\"\n",
    "\n",
    "clientes_crm= pd.read_json(\"clientes_crm.json\")\n",
    "custo_importacao= pd.read_json(\"custos_importacao.json\")\n",
    "#clientes_crm.head()\n",
    "#custo_importacao.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "8499e0da-a719-4b39-b71a-8e83dedd1d0e",
   "metadata": {},
   "outputs": [],
   "source": [
    "\"\"\"dados csv\n",
    "Nesta carrego os csv\"\"\"\n",
    "\n",
    "produtos= pd.read_csv(\"produtos_raw.csv\")\n",
    "vendas= pd.read_csv(\"vendas_2023_2024.csv\")\n",
    "#produtos.head()\n",
    "#vendas.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d1e0f5c5-c57e-470d-914d-931c55a834ff",
   "metadata": {},
   "source": [
    "## Analise da base de cliente e tratamento"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "144492cd-3006-466c-9e4d-9129b94bdacc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['full_name', 'location', 'code', 'email'], dtype='str')"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#identificando as colunas\n",
    "clientes_crm.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "id": "f0856370-39fc-4249-8b49-6ec03b1b520a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "location\n",
       "BA - Porto Seguro                 2\n",
       "Aratu (Candeias) , BA             1\n",
       "PE , Recife                       1\n",
       "Rio Grande,RS                     1\n",
       "AC , Rio Branco                   1\n",
       "PA - Santarém Novo                1\n",
       "Fortaleza do Tabocão , TO         1\n",
       "PB/Cabedelo                       1\n",
       "SE - Aracaju                      1\n",
       "PB - João Pessoa                  1\n",
       "Santarém / PA                     1\n",
       "TO , Fortaleza do Tabocão         1\n",
       "PA / Santarém                     1\n",
       "AM , Itacoatiara                  1\n",
       "Fortaleza do Tabocão,TO           1\n",
       "Fortaleza,CE                      1\n",
       "MS - Corumbá                      1\n",
       "Santarém - PA                     1\n",
       "Maceió / AL                       1\n",
       "PA , Santarém Novo                1\n",
       "AC,Rio Branco                     1\n",
       "SE / Aracaju                      1\n",
       "Santos - SP                       1\n",
       "Laguna / SC                       1\n",
       "ES / São Mateus                   1\n",
       "Manaus/AM                         1\n",
       "Salvador,BA                       1\n",
       "PR , Antonina                     1\n",
       "CE,Fortaleza                      1\n",
       "Itacoatiara - AM                  1\n",
       "São Luís,MA                       1\n",
       "Rio Grande/RS                     1\n",
       "Fortaleza / CE                    1\n",
       "João Pessoa / PB                  1\n",
       "Belém/PA                          1\n",
       "MA , Itaqui (São Luís)            1\n",
       "TO/Fortaleza do Tabocão           1\n",
       "PE / Suape (Ipojuca)              1\n",
       "Corumbá,MS                        1\n",
       "BA / Aratu (Candeias)             1\n",
       "Vila do Conde (Barcarena) - PA    1\n",
       "MA/Itaqui (São Luís)              1\n",
       "Paranaguá / PR                    1\n",
       "Santarém,PA                       1\n",
       "Macapá/AP                         1\n",
       "RJ / Niterói                      1\n",
       "PE - Suape (Ipojuca)              1\n",
       "SE/Aracaju                        1\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 94,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#nessa celula identifiquei que os nomes das localizações estava sem tratamento e desorganizado\n",
    "clientes_crm.head\n",
    "clientes_crm[\"location\"].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "25309689-5ccf-4afb-96a5-e57346889295",
   "metadata": {},
   "outputs": [],
   "source": [
    "#padronização do texto\n",
    "clientes_crm[\"location\"] = clientes_crm[\"location\"].str.strip()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "94b672c7-ae54-4989-931e-eaa88c4ac611",
   "metadata": {},
   "outputs": [],
   "source": [
    "#extrair estado\n",
    "clientes_crm[\"estado\"] = clientes_crm[\"location\"].str.extract(r'([A-Z]{2})')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "c969d777-bd6f-4ed1-a284-044c43c295a3",
   "metadata": {},
   "outputs": [],
   "source": [
    "#extrair cidade\n",
    "clientes_crm[\"cidade\"] = clientes_crm[\"location\"].str.replace(r'[A-Z]{2}', '', regex=True)\n",
    "clientes_crm[\"cidade\"] = clientes_crm[\"cidade\"].str.replace(r'[-,/()]', '', regex=True).str.strip()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "id": "fd9b30d3-df29-455d-987a-917b95c30a71",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>full_name</th>\n",
       "      <th>location</th>\n",
       "      <th>client_id</th>\n",
       "      <th>email</th>\n",
       "      <th>estado</th>\n",
       "      <th>cidade</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Femininos Oliveira Antunes</td>\n",
       "      <td>Aratu (Candeias) , BA</td>\n",
       "      <td>1</td>\n",
       "      <td>femininos.oliveira.antunes@icloud.com</td>\n",
       "      <td>BA</td>\n",
       "      <td>Aratu Candeias</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Fernanda Azevedo Soares Nunes Vieira</td>\n",
       "      <td>PE , Recife</td>\n",
       "      <td>2</td>\n",
       "      <td>nunes.fernanda.soares.azevedo.vieira@outlook.com</td>\n",
       "      <td>PE</td>\n",
       "      <td>Recife</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Daniel Farias Ribeiro Teixeira</td>\n",
       "      <td>Rio Grande,RS</td>\n",
       "      <td>3</td>\n",
       "      <td>farias.teixeira.daniel.ribeiro#gmail.com</td>\n",
       "      <td>RS</td>\n",
       "      <td>Rio Grande</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Thiago Moreira</td>\n",
       "      <td>AC , Rio Branco</td>\n",
       "      <td>4</td>\n",
       "      <td>thiago.moreira#gmail.com</td>\n",
       "      <td>AC</td>\n",
       "      <td>Rio Branco</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Pedro Freitas</td>\n",
       "      <td>PA - Santarém Novo</td>\n",
       "      <td>5</td>\n",
       "      <td>pedro.freitas#icloud.com</td>\n",
       "      <td>PA</td>\n",
       "      <td>Santarém Novo</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                              full_name               location  client_id  \\\n",
       "0            Femininos Oliveira Antunes  Aratu (Candeias) , BA          1   \n",
       "1  Fernanda Azevedo Soares Nunes Vieira            PE , Recife          2   \n",
       "2        Daniel Farias Ribeiro Teixeira          Rio Grande,RS          3   \n",
       "3                        Thiago Moreira        AC , Rio Branco          4   \n",
       "4                         Pedro Freitas     PA - Santarém Novo          5   \n",
       "\n",
       "                                              email estado          cidade  \n",
       "0             femininos.oliveira.antunes@icloud.com     BA  Aratu Candeias  \n",
       "1  nunes.fernanda.soares.azevedo.vieira@outlook.com     PE          Recife  \n",
       "2          farias.teixeira.daniel.ribeiro#gmail.com     RS      Rio Grande  \n",
       "3                          thiago.moreira#gmail.com     AC      Rio Branco  \n",
       "4                          pedro.freitas#icloud.com     PA   Santarém Novo  "
      ]
     },
     "execution_count": 95,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# temos a coluna original location e as que criei apenas com estados e ao lado apenas com a cidade\n",
    "clientes_crm.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "22565fd1-ed01-4555-beb7-cdc0fb5ad50b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "full_name      str\n",
       "location       str\n",
       "code         int64\n",
       "email          str\n",
       "estado         str\n",
       "cidade         str\n",
       "dtype: object"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#identificação dos tipos de dados\n",
    "clientes_crm.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "3cbfe8ac-2324-461b-b20c-8092608bf0a8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.DataFrame'>\n",
      "RangeIndex: 49 entries, 0 to 48\n",
      "Data columns (total 6 columns):\n",
      " #   Column     Non-Null Count  Dtype\n",
      "---  ------     --------------  -----\n",
      " 0   full_name  49 non-null     str  \n",
      " 1   location   49 non-null     str  \n",
      " 2   code       49 non-null     int64\n",
      " 3   email      49 non-null     str  \n",
      " 4   estado     49 non-null     str  \n",
      " 5   cidade     49 non-null     str  \n",
      "dtypes: int64(1), str(5)\n",
      "memory usage: 2.4 KB\n"
     ]
    }
   ],
   "source": [
    "clientes_crm.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "ad8ed054-2711-427e-a2d3-aa6023776562",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "full_name    0\n",
       "location     0\n",
       "code         0\n",
       "email        0\n",
       "estado       0\n",
       "cidade       0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "clientes_crm.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "443356d4-061a-4146-a335-80c5a436e8e2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "np.int64(0)"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "clientes_crm.duplicated().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "158b2365-0870-4c99-b0d1-d91ae67e835b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>full_name</th>\n",
       "      <th>location</th>\n",
       "      <th>client_id</th>\n",
       "      <th>email</th>\n",
       "      <th>estado</th>\n",
       "      <th>cidade</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Femininos Oliveira Antunes</td>\n",
       "      <td>Aratu (Candeias) , BA</td>\n",
       "      <td>1</td>\n",
       "      <td>femininos.oliveira.antunes@icloud.com</td>\n",
       "      <td>BA</td>\n",
       "      <td>Aratu Candeias</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Fernanda Azevedo Soares Nunes Vieira</td>\n",
       "      <td>PE , Recife</td>\n",
       "      <td>2</td>\n",
       "      <td>nunes.fernanda.soares.azevedo.vieira@outlook.com</td>\n",
       "      <td>PE</td>\n",
       "      <td>Recife</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Daniel Farias Ribeiro Teixeira</td>\n",
       "      <td>Rio Grande,RS</td>\n",
       "      <td>3</td>\n",
       "      <td>farias.teixeira.daniel.ribeiro#gmail.com</td>\n",
       "      <td>RS</td>\n",
       "      <td>Rio Grande</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Thiago Moreira</td>\n",
       "      <td>AC , Rio Branco</td>\n",
       "      <td>4</td>\n",
       "      <td>thiago.moreira#gmail.com</td>\n",
       "      <td>AC</td>\n",
       "      <td>Rio Branco</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Pedro Freitas</td>\n",
       "      <td>PA - Santarém Novo</td>\n",
       "      <td>5</td>\n",
       "      <td>pedro.freitas#icloud.com</td>\n",
       "      <td>PA</td>\n",
       "      <td>Santarém Novo</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                              full_name               location  client_id  \\\n",
       "0            Femininos Oliveira Antunes  Aratu (Candeias) , BA          1   \n",
       "1  Fernanda Azevedo Soares Nunes Vieira            PE , Recife          2   \n",
       "2        Daniel Farias Ribeiro Teixeira          Rio Grande,RS          3   \n",
       "3                        Thiago Moreira        AC , Rio Branco          4   \n",
       "4                         Pedro Freitas     PA - Santarém Novo          5   \n",
       "\n",
       "                                              email estado          cidade  \n",
       "0             femininos.oliveira.antunes@icloud.com     BA  Aratu Candeias  \n",
       "1  nunes.fernanda.soares.azevedo.vieira@outlook.com     PE          Recife  \n",
       "2          farias.teixeira.daniel.ribeiro#gmail.com     RS      Rio Grande  \n",
       "3                          thiago.moreira#gmail.com     AC      Rio Branco  \n",
       "4                          pedro.freitas#icloud.com     PA   Santarém Novo  "
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "clientes_crm = clientes_crm.rename(columns={\"code\": \"client_id\"})\n",
    "clientes_crm.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b3dd9168-0fee-4989-a7e4-b8821cd5de80",
   "metadata": {},
   "source": [
    "## Tratamento base de clientes -- localidade\n",
    "\n",
    "A coluna `location` apresentava formatos inconsistentes, com variações\n",
    "na forma de representação de cidade e estado.\n",
    "\n",
    "Foi realizada a extração das informações de estado e cidade, permitindo\n",
    "padronização e facilitando análises geográficas futuras, mantive os dados brutos\n",
    "de location.\n",
    "\n",
    "durante a exploração de dados conclui-se que a base de dados de clientes não existe nulos e duplicatas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b88c69d4-a1da-4d3f-b24d-bd907b2a99bb",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "0e0539f0-70ec-4a67-be08-95cf5892a370",
   "metadata": {},
   "source": [
    "## Analise da base de custo de importação"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "601c199f-a190-4502-9c7a-b2944d354690",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['product_id', 'product_name', 'category', 'historic_data'], dtype='str')"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#identificando as colunas\n",
    "custo_importacao.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "38097de7-b8ad-4630-b122-bb854f1c0551",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "product_id        int64\n",
       "product_name        str\n",
       "category            str\n",
       "historic_data    object\n",
       "dtype: object"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#identificação dos tipos de dados\n",
    "#obs: historic_data esta como object e vai ser tratada\n",
    "custo_importacao.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "64a01078-53b4-485b-b558-bb47295b541f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.DataFrame'>\n",
      "RangeIndex: 150 entries, 0 to 149\n",
      "Data columns (total 4 columns):\n",
      " #   Column         Non-Null Count  Dtype \n",
      "---  ------         --------------  ----- \n",
      " 0   product_id     150 non-null    int64 \n",
      " 1   product_name   150 non-null    str   \n",
      " 2   category       150 non-null    str   \n",
      " 3   historic_data  150 non-null    object\n",
      "dtypes: int64(1), object(1), str(2)\n",
      "memory usage: 4.8+ KB\n"
     ]
    }
   ],
   "source": [
    "custo_importacao.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "36677319-4d67-4133-8d16-14a50445daed",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "product_id       0\n",
       "product_name     0\n",
       "category         0\n",
       "historic_data    0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#identificação de nulos\n",
    "custo_importacao.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "8e28d59f-4a97-44f2-9adb-87412c2356cc",
   "metadata": {},
   "outputs": [],
   "source": [
    "#tratamento do campo historic_data\n",
    "custo_importacao[\"historic_data\"] = custo_importacao[\"historic_data\"].apply(\n",
    "    lambda x: ast.literal_eval(x) if isinstance(x, str) else x\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "c31d5e21-d172-4fbb-82f6-66e28f39ace0",
   "metadata": {},
   "outputs": [],
   "source": [
    "custo_importacao = custo_importacao.explode(\"historic_data\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "1318aed2-5eb6-4c2a-a841-98a4f928fb89",
   "metadata": {},
   "outputs": [],
   "source": [
    "historic_df = pd.json_normalize(custo_importacao[\"historic_data\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "d66c5752-d1b2-4a9e-8311-c4b356f9a3fc",
   "metadata": {},
   "outputs": [],
   "source": [
    "custo_importacao_tratado = pd.concat(\n",
    "    [custo_importacao.drop(columns=[\"historic_data\"]), historic_df],\n",
    "    axis=1\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "7dcf7110-dafb-4d9a-9922-2d5f25207490",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>product_id</th>\n",
       "      <th>product_name</th>\n",
       "      <th>category</th>\n",
       "      <th>start_date</th>\n",
       "      <th>usd_price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Transponder AIS Maré Magnum</td>\n",
       "      <td>eletrônicos</td>\n",
       "      <td>10/08/2016</td>\n",
       "      <td>10583.63</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Transponder AIS Maré Magnum</td>\n",
       "      <td>eletrônicos</td>\n",
       "      <td>15/06/2018</td>\n",
       "      <td>8778.36</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Transponder AIS Maré Magnum</td>\n",
       "      <td>eletrônicos</td>\n",
       "      <td>25/09/2018</td>\n",
       "      <td>8023.87</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Transponder AIS Maré Magnum</td>\n",
       "      <td>eletrônicos</td>\n",
       "      <td>19/03/2019</td>\n",
       "      <td>8772.78</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Transponder AIS Maré Magnum</td>\n",
       "      <td>eletrônicos</td>\n",
       "      <td>17/01/2020</td>\n",
       "      <td>7918.18</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   product_id                 product_name     category  start_date  usd_price\n",
       "0           1  Transponder AIS Maré Magnum  eletrônicos  10/08/2016   10583.63\n",
       "0           1  Transponder AIS Maré Magnum  eletrônicos  15/06/2018    8778.36\n",
       "0           1  Transponder AIS Maré Magnum  eletrônicos  25/09/2018    8023.87\n",
       "0           1  Transponder AIS Maré Magnum  eletrônicos  19/03/2019    8772.78\n",
       "0           1  Transponder AIS Maré Magnum  eletrônicos  17/01/2020    7918.18"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "custo_importacao_tratado.head()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "6d17d63e-925e-4799-8370-70f970026e6a",
   "metadata": {},
   "outputs": [],
   "source": [
    "custo_importacao_tratado[\"start_date\"] = pd.to_datetime(\n",
    "    custo_importacao_tratado[\"start_date\"], \n",
    "    dayfirst=True,\n",
    "    errors=\"coerce\"\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "2cd780e1-b82c-4e25-bc35-9c3e7b4bc2e1",
   "metadata": {},
   "outputs": [],
   "source": [
    "#separação das tabelas de custo historico e custo final\n",
    "custo_historico = custo_importacao_tratado.copy()\n",
    "\n",
    "custo_final = (\n",
    "    custo_importacao_tratado\n",
    "    .sort_values(\"start_date\")\n",
    "    .groupby(\"product_id\")\n",
    "    .tail(1)\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "782273d2-3418-4a2e-84c6-28cee323b258",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "category\n",
       "eletrônicos    436\n",
       "ancoragem      413\n",
       "propulsão      411\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "custo_historico [\"category\"].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "6dc19374-3c5c-4121-8059-31ed81aa4d0d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "category\n",
       "ancoragem      50\n",
       "eletrônicos    50\n",
       "propulsão      50\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "custo_final[\"category\"].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "dd913dc9-ce0c-4b29-afee-3dff79cd0cfd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>product_id</th>\n",
       "      <th>product_name</th>\n",
       "      <th>category</th>\n",
       "      <th>start_date</th>\n",
       "      <th>usd_price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>103</th>\n",
       "      <td>104</td>\n",
       "      <td>Cabo de Nylon Delta Zen Vortex Storm</td>\n",
       "      <td>ancoragem</td>\n",
       "      <td>2020-03-26</td>\n",
       "      <td>742.54</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>38</th>\n",
       "      <td>39</td>\n",
       "      <td>GPS Furuno Vector</td>\n",
       "      <td>eletrônicos</td>\n",
       "      <td>2020-10-16</td>\n",
       "      <td>5270.87</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>125</th>\n",
       "      <td>126</td>\n",
       "      <td>Corrente Danforth Hydro</td>\n",
       "      <td>ancoragem</td>\n",
       "      <td>2020-10-28</td>\n",
       "      <td>467.05</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>138</th>\n",
       "      <td>139</td>\n",
       "      <td>Boia de Arqueamento Danforth Torque</td>\n",
       "      <td>ancoragem</td>\n",
       "      <td>2020-10-30</td>\n",
       "      <td>246.89</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>53</th>\n",
       "      <td>54</td>\n",
       "      <td>Motor de Popa Yamaha Evo Dash 155HP</td>\n",
       "      <td>propulsão</td>\n",
       "      <td>2021-08-06</td>\n",
       "      <td>23191.90</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     product_id                          product_name     category start_date  \\\n",
       "103         104  Cabo de Nylon Delta Zen Vortex Storm    ancoragem 2020-03-26   \n",
       "38           39                     GPS Furuno Vector  eletrônicos 2020-10-16   \n",
       "125         126               Corrente Danforth Hydro    ancoragem 2020-10-28   \n",
       "138         139   Boia de Arqueamento Danforth Torque    ancoragem 2020-10-30   \n",
       "53           54   Motor de Popa Yamaha Evo Dash 155HP    propulsão 2021-08-06   \n",
       "\n",
       "     usd_price  \n",
       "103     742.54  \n",
       "38     5270.87  \n",
       "125     467.05  \n",
       "138     246.89  \n",
       "53    23191.90  "
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "custo_final.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "80ebf2c3-97df-4a3d-8fd0-4d43eb11d83f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "product_id               int64\n",
       "product_name               str\n",
       "category                   str\n",
       "start_date      datetime64[us]\n",
       "usd_price              float64\n",
       "dtype: object"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "custo_final.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "c165eb91-56d5-4a40-8ade-fe5524b1dae6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>product_id</th>\n",
       "      <th>product_name</th>\n",
       "      <th>category</th>\n",
       "      <th>start_date</th>\n",
       "      <th>usd_price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>149</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>149</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>149</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>149</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>149</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1260 rows × 5 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     product_id  product_name  category  start_date  usd_price\n",
       "0         False         False     False       False      False\n",
       "0         False         False     False       False      False\n",
       "0         False         False     False       False      False\n",
       "0         False         False     False       False      False\n",
       "0         False         False     False       False      False\n",
       "..          ...           ...       ...         ...        ...\n",
       "149       False         False     False       False      False\n",
       "149       False         False     False       False      False\n",
       "149       False         False     False       False      False\n",
       "149       False         False     False       False      False\n",
       "149       False         False     False       False      False\n",
       "\n",
       "[1260 rows x 5 columns]"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "custo_historico.isnull()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "c20a8d58-a8ff-43bd-b730-2d46674ed33e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.DataFrame'>\n",
      "Index: 150 entries, 103 to 24\n",
      "Data columns (total 5 columns):\n",
      " #   Column        Non-Null Count  Dtype         \n",
      "---  ------        --------------  -----         \n",
      " 0   product_id    150 non-null    int64         \n",
      " 1   product_name  150 non-null    str           \n",
      " 2   category      150 non-null    str           \n",
      " 3   start_date    150 non-null    datetime64[us]\n",
      " 4   usd_price     150 non-null    float64       \n",
      "dtypes: datetime64[us](1), float64(1), int64(1), str(2)\n",
      "memory usage: 7.0 KB\n"
     ]
    }
   ],
   "source": [
    "custo_final.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "83807ca1-0c48-4c3d-a2ca-d39912bfc2d5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>product_id</th>\n",
       "      <th>product_name</th>\n",
       "      <th>category</th>\n",
       "      <th>start_date</th>\n",
       "      <th>usd_price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Transponder AIS Maré Magnum</td>\n",
       "      <td>eletrônicos</td>\n",
       "      <td>2016-08-10</td>\n",
       "      <td>10583.63</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Transponder AIS Maré Magnum</td>\n",
       "      <td>eletrônicos</td>\n",
       "      <td>2018-06-15</td>\n",
       "      <td>8778.36</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Transponder AIS Maré Magnum</td>\n",
       "      <td>eletrônicos</td>\n",
       "      <td>2018-09-25</td>\n",
       "      <td>8023.87</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Transponder AIS Maré Magnum</td>\n",
       "      <td>eletrônicos</td>\n",
       "      <td>2019-03-19</td>\n",
       "      <td>8772.78</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Transponder AIS Maré Magnum</td>\n",
       "      <td>eletrônicos</td>\n",
       "      <td>2020-01-17</td>\n",
       "      <td>7918.18</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   product_id                 product_name     category start_date  usd_price\n",
       "0           1  Transponder AIS Maré Magnum  eletrônicos 2016-08-10   10583.63\n",
       "0           1  Transponder AIS Maré Magnum  eletrônicos 2018-06-15    8778.36\n",
       "0           1  Transponder AIS Maré Magnum  eletrônicos 2018-09-25    8023.87\n",
       "0           1  Transponder AIS Maré Magnum  eletrônicos 2019-03-19    8772.78\n",
       "0           1  Transponder AIS Maré Magnum  eletrônicos 2020-01-17    7918.18"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "custo_historico.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "df674868-3069-4a0d-b878-dff0313f3684",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "59d9d7e5-4a2e-4fd2-a78f-fa0f1f56f1f0",
   "metadata": {},
   "source": [
    " \n",
    "## Tratamento da coluna historic_data e conclusão da base de importação\n",
    "Foi identificado que a coluna `historic_data` continha listas de registros\n",
    "históricos de preços em formato JSON.\n",
    "\n",
    "Para permitir a análise temporal dos custos, os dados foram:\n",
    "\n",
    "1. Convertidos de string para estrutura de lista\n",
    "2. Expandido para múltiplas linhas (uma por registro histórico)\n",
    "3. Normalizados em colunas estruturadas\n",
    "\n",
    "Após a normalização da coluna `historic_data`, observou-se um aumento no número\n",
    "de linhas devido à existência de múltiplos registros históricos por produto.\n",
    "A tabela custo_historico será usada para possiveis analises temporais\n",
    "\n",
    "Para a análise principal, foi considerada a versão mais recente do custo,\n",
    "representando o valor atual de importação, representada na tabela Custo_final\n",
    "\n",
    "Conclui-se que a base de dados de custo importação não apresenta nulos"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7176d339-2173-4297-853f-fefd25238447",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "756fda70-2139-451e-a93f-fe366922f7a8",
   "metadata": {},
   "source": [
    "## Analise da base de produtos"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "a116bdf3-317a-4cf2-95d7-3f761ee3c5cb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['name', 'price', 'code', 'actual_category'], dtype='str')"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#identificando as colunas\n",
    "produtos.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "6dcae19a-97ed-4c98-915c-fbd7250be20a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "name                 str\n",
       "price                str\n",
       "code               int64\n",
       "actual_category      str\n",
       "dtype: object"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "produtos.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "143f2e7a-57a4-4ca0-a65c-402df7597d67",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>name</th>\n",
       "      <th>price</th>\n",
       "      <th>code</th>\n",
       "      <th>actual_category</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Transponder AIS Maré Magnum</td>\n",
       "      <td>R$ 33122.52</td>\n",
       "      <td>1</td>\n",
       "      <td>ELETRONICOS</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Transponder Furuno Marlin</td>\n",
       "      <td>R$ 13998.15</td>\n",
       "      <td>2</td>\n",
       "      <td>ELETRONICOS</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Radar Furuno Pulse Leviathan</td>\n",
       "      <td>R$ 9024.19</td>\n",
       "      <td>3</td>\n",
       "      <td>E L E T R Ô N I C O S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Rádio AIS Hydro Tidal Zen</td>\n",
       "      <td>R$ 3381.88</td>\n",
       "      <td>4</td>\n",
       "      <td>Eletrunicos</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Piloto Automático Furuno Storm</td>\n",
       "      <td>R$ 23669.01</td>\n",
       "      <td>5</td>\n",
       "      <td>Eletronicoz</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                             name        price  code        actual_category\n",
       "0     Transponder AIS Maré Magnum  R$ 33122.52     1            ELETRONICOS\n",
       "1       Transponder Furuno Marlin  R$ 13998.15     2            ELETRONICOS\n",
       "2    Radar Furuno Pulse Leviathan   R$ 9024.19     3  E L E T R Ô N I C O S\n",
       "3       Rádio AIS Hydro Tidal Zen   R$ 3381.88     4            Eletrunicos\n",
       "4  Piloto Automático Furuno Storm  R$ 23669.01     5            Eletronicoz"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#padronizar as categorias atuais\n",
    "#preço esta como str colocar como numeric\n",
    "produtos.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "eb93d346-4880-4b13-a94f-5c209f095f3b",
   "metadata": {},
   "outputs": [],
   "source": [
    "#corrigindo variações da categoria, Padronização\n",
    "def limpar_texto(texto):\n",
    "    texto = texto.lower().strip()\n",
    "    texto = ''.join(\n",
    "        c for c in unicodedata.normalize('NFKD', texto)\n",
    "        if not unicodedata.combining(c)\n",
    "    )\n",
    "    texto = texto.replace(\" \", \"\")\n",
    "    return texto\n",
    "\n",
    "produtos[\"actual_category\"] = produtos[\"actual_category\"].apply(limpar_texto)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "d05416a9-cc0a-412a-a049-7a474ecb2104",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>name</th>\n",
       "      <th>price</th>\n",
       "      <th>code</th>\n",
       "      <th>actual_category</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Transponder AIS Maré Magnum</td>\n",
       "      <td>R$ 33122.52</td>\n",
       "      <td>1</td>\n",
       "      <td>eletronicos</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Transponder Furuno Marlin</td>\n",
       "      <td>R$ 13998.15</td>\n",
       "      <td>2</td>\n",
       "      <td>eletronicos</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Radar Furuno Pulse Leviathan</td>\n",
       "      <td>R$ 9024.19</td>\n",
       "      <td>3</td>\n",
       "      <td>eletronicos</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Rádio AIS Hydro Tidal Zen</td>\n",
       "      <td>R$ 3381.88</td>\n",
       "      <td>4</td>\n",
       "      <td>eletrunicos</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Piloto Automático Furuno Storm</td>\n",
       "      <td>R$ 23669.01</td>\n",
       "      <td>5</td>\n",
       "      <td>eletronicoz</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>95</th>\n",
       "      <td>Motor Elétrico Yamaha Nautic Kraken 133HP</td>\n",
       "      <td>R$ 88854.1</td>\n",
       "      <td>92</td>\n",
       "      <td>propucao</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>96</th>\n",
       "      <td>Motor Elétrico Yamaha Flow 204HP</td>\n",
       "      <td>R$ 100477.01</td>\n",
       "      <td>93</td>\n",
       "      <td>propulsao</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>97</th>\n",
       "      <td>Motor de Popa Volvo Magnum 276HP</td>\n",
       "      <td>R$ 40750.84</td>\n",
       "      <td>94</td>\n",
       "      <td>propucao</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>98</th>\n",
       "      <td>Motor Diesel Honda Leviathan 133HP</td>\n",
       "      <td>R$ 69808.04</td>\n",
       "      <td>95</td>\n",
       "      <td>propulsao</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>99</th>\n",
       "      <td>Motor de Popa Tohatsu Boost Swift 126HP</td>\n",
       "      <td>R$ 70620.84</td>\n",
       "      <td>96</td>\n",
       "      <td>propulssao</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>100 rows × 4 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                                         name         price  code  \\\n",
       "0                 Transponder AIS Maré Magnum   R$ 33122.52     1   \n",
       "1                   Transponder Furuno Marlin   R$ 13998.15     2   \n",
       "2                Radar Furuno Pulse Leviathan    R$ 9024.19     3   \n",
       "3                   Rádio AIS Hydro Tidal Zen    R$ 3381.88     4   \n",
       "4              Piloto Automático Furuno Storm   R$ 23669.01     5   \n",
       "..                                        ...           ...   ...   \n",
       "95  Motor Elétrico Yamaha Nautic Kraken 133HP    R$ 88854.1    92   \n",
       "96           Motor Elétrico Yamaha Flow 204HP  R$ 100477.01    93   \n",
       "97           Motor de Popa Volvo Magnum 276HP   R$ 40750.84    94   \n",
       "98         Motor Diesel Honda Leviathan 133HP   R$ 69808.04    95   \n",
       "99    Motor de Popa Tohatsu Boost Swift 126HP   R$ 70620.84    96   \n",
       "\n",
       "   actual_category  \n",
       "0      eletronicos  \n",
       "1      eletronicos  \n",
       "2      eletronicos  \n",
       "3      eletrunicos  \n",
       "4      eletronicoz  \n",
       "..             ...  \n",
       "95        propucao  \n",
       "96       propulsao  \n",
       "97        propucao  \n",
       "98       propulsao  \n",
       "99      propulssao  \n",
       "\n",
       "[100 rows x 4 columns]"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "produtos.head(100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "406da34a-eb9b-46b5-8721-2dfd2f75489c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# substituindo as categorias\n",
    "mapa = {\n",
    "    \"eletroniscos\": \"eletrônicos\",\n",
    "    \"eletronicoz\" : \"eletrônicos\",\n",
    "    \"eletrunicos\": \"eletrônicos\",\n",
    "    \"eletronicos\": \"eletrônicos\",\n",
    "    \"prop\": \"propulsão\",\n",
    "    \"propulsao\": \"propulsão\",\n",
    "    \"propulcao\": \"propulsão\",\n",
    "    \"propulsam\": \"propulsão\",\n",
    "    \"propucao\" : \"propulsão\",\n",
    "    \"propulssao\" : \"propulsão\",\n",
    "    \"ancorajem\": \"ancoragem\",\n",
    "    \"ancoragen\": \"ancoragem\",\n",
    "    \"encoragem\": \"ancoragem\",\n",
    "    \"encoragi\": \"ancoragem\",\n",
    "    \"ancorajm\": \"ancoragem\",\n",
    "    \"ancorajen\": \"ancoragem\",\n",
    "    \"ancoraguem\": \"ancoragem\"\n",
    "}\n",
    "\n",
    "produtos[\"actual_category\"] = produtos[\"actual_category\"].replace(mapa)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "5732d3c5-1544-43f8-bfab-9e7f10c546cd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "actual_category\n",
       "propulsão      53\n",
       "ancoragem      53\n",
       "eletrônicos    51\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "produtos[\"actual_category\"].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "3af7fb15-f8ad-4691-adff-a71adc50cb42",
   "metadata": {},
   "outputs": [],
   "source": [
    "# corrigindo o tipo de dado\n",
    "produtos[\"price\"] = (\n",
    "    produtos[\"price\"]\n",
    "    .str.replace(\"R$\", \"\", regex=False)\n",
    "    .str.strip()\n",
    "    .astype(float)\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "679ab8e7-3c4c-45a5-9ea7-5ffa61a8bb94",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.DataFrame'>\n",
      "RangeIndex: 157 entries, 0 to 156\n",
      "Data columns (total 4 columns):\n",
      " #   Column           Non-Null Count  Dtype  \n",
      "---  ------           --------------  -----  \n",
      " 0   name             157 non-null    str    \n",
      " 1   price            157 non-null    float64\n",
      " 2   code             157 non-null    int64  \n",
      " 3   actual_category  157 non-null    str    \n",
      "dtypes: float64(1), int64(1), str(2)\n",
      "memory usage: 5.0 KB\n"
     ]
    }
   ],
   "source": [
    "produtos.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "36a66a62-709a-4b67-8ebd-bc2a25604828",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "name               0\n",
       "price              0\n",
       "code               0\n",
       "actual_category    0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "produtos.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "91717eb3-c9da-40a8-ad91-d759076c0af7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "np.int64(7)"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "produtos.duplicated().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "0fdf36e2-f4ec-4850-82ac-33bfd34576dd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>name</th>\n",
       "      <th>price</th>\n",
       "      <th>product_id</th>\n",
       "      <th>actual_category</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Transponder AIS Maré Magnum</td>\n",
       "      <td>33122.52</td>\n",
       "      <td>1</td>\n",
       "      <td>eletrônicos</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Transponder Furuno Marlin</td>\n",
       "      <td>13998.15</td>\n",
       "      <td>2</td>\n",
       "      <td>eletrônicos</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Radar Furuno Pulse Leviathan</td>\n",
       "      <td>9024.19</td>\n",
       "      <td>3</td>\n",
       "      <td>eletrônicos</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Rádio AIS Hydro Tidal Zen</td>\n",
       "      <td>3381.88</td>\n",
       "      <td>4</td>\n",
       "      <td>eletrônicos</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Piloto Automático Furuno Storm</td>\n",
       "      <td>23669.01</td>\n",
       "      <td>5</td>\n",
       "      <td>eletrônicos</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                             name     price  product_id actual_category\n",
       "0     Transponder AIS Maré Magnum  33122.52           1     eletrônicos\n",
       "1       Transponder Furuno Marlin  13998.15           2     eletrônicos\n",
       "2    Radar Furuno Pulse Leviathan   9024.19           3     eletrônicos\n",
       "3       Rádio AIS Hydro Tidal Zen   3381.88           4     eletrônicos\n",
       "4  Piloto Automático Furuno Storm  23669.01           5     eletrônicos"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "produtos = produtos.rename(columns={\"code\": \"product_id\"})\n",
    "produtos.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a194d72b-d28c-4330-8142-c6cf76ff3f06",
   "metadata": {},
   "source": [
    "## Padronização de categorias\n",
    "\n",
    "Foram identificadas diversas inconsistências na coluna `actual_category`,\n",
    "incluindo variações de acentuação, espaçamento e erros de digitação.\n",
    "\n",
    "Foi aplicada uma função de limpeza para normalizar os textos, incluindo:\n",
    "\n",
    "- conversão para minúsculas\n",
    "- remoção de acentos\n",
    "- remoção de espaços\n",
    "\n",
    "Em seguida, foi criado um mapeamento manual para corrigir variações\n",
    "identificadas, consolidando as categorias em valores únicos e consistentes.\n",
    "Outros passos incluem a verificação de nulos nas quais não temos nulos e verificação de duplicatas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e02dad9a-0944-4428-b5fd-b9db0df49f2d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "770bb3f9-88a5-4e2b-9a6f-7db430ed9cce",
   "metadata": {},
   "source": [
    "## Analise da base de vendas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "e79eb386-481d-47dd-bbe4-4c89291c2607",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['id', 'id_client', 'id_product', 'qtd', 'total', 'sale_date'], dtype='str')"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#verificando as colunas\n",
    "vendas.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "5772ef25-9297-4adb-accd-16a7bec8e94d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "id              int64\n",
       "id_client       int64\n",
       "id_product      int64\n",
       "qtd             int64\n",
       "total         float64\n",
       "sale_date         str\n",
       "dtype: object"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#verificando os tipos de dados\n",
    "# sales_dates deve ser convertido para Date\n",
    "vendas.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "e46d766b-9cda-4312-82ad-ed56b8bfde08",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>id_client</th>\n",
       "      <th>id_product</th>\n",
       "      <th>qtd</th>\n",
       "      <th>total</th>\n",
       "      <th>sale_date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "Empty DataFrame\n",
       "Columns: [id, id_client, id_product, qtd, total, sale_date]\n",
       "Index: []"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "vendas[vendas[\"sale_date\"].isnull()]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "da4098a0-c513-463b-a939-cfaef4f8d9fc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>id_client</th>\n",
       "      <th>id_product</th>\n",
       "      <th>qtd</th>\n",
       "      <th>total</th>\n",
       "      <th>sale_date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>42</td>\n",
       "      <td>105</td>\n",
       "      <td>11</td>\n",
       "      <td>3405.00</td>\n",
       "      <td>2023-09-10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>136</td>\n",
       "      <td>9</td>\n",
       "      <td>16873.90</td>\n",
       "      <td>15-09-2024</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>25</td>\n",
       "      <td>139</td>\n",
       "      <td>7</td>\n",
       "      <td>9475.30</td>\n",
       "      <td>2024-08-13</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>20</td>\n",
       "      <td>23</td>\n",
       "      <td>5</td>\n",
       "      <td>55893.00</td>\n",
       "      <td>2023-02-03</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>8</td>\n",
       "      <td>57</td>\n",
       "      <td>4</td>\n",
       "      <td>451403.90</td>\n",
       "      <td>2024-02-12</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>95</th>\n",
       "      <td>98</td>\n",
       "      <td>21</td>\n",
       "      <td>142</td>\n",
       "      <td>2</td>\n",
       "      <td>1570.35</td>\n",
       "      <td>2024-02-13</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>96</th>\n",
       "      <td>99</td>\n",
       "      <td>49</td>\n",
       "      <td>81</td>\n",
       "      <td>9</td>\n",
       "      <td>1099336.00</td>\n",
       "      <td>06-01-2024</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>97</th>\n",
       "      <td>100</td>\n",
       "      <td>22</td>\n",
       "      <td>93</td>\n",
       "      <td>4</td>\n",
       "      <td>381812.60</td>\n",
       "      <td>21-01-2023</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>98</th>\n",
       "      <td>101</td>\n",
       "      <td>11</td>\n",
       "      <td>47</td>\n",
       "      <td>8</td>\n",
       "      <td>48984.00</td>\n",
       "      <td>04-07-2024</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>99</th>\n",
       "      <td>102</td>\n",
       "      <td>9</td>\n",
       "      <td>67</td>\n",
       "      <td>9</td>\n",
       "      <td>733495.95</td>\n",
       "      <td>2024-02-02</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>100 rows × 6 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     id  id_client  id_product  qtd       total   sale_date\n",
       "0     0         42         105   11     3405.00  2023-09-10\n",
       "1     1          3         136    9    16873.90  15-09-2024\n",
       "2     2         25         139    7     9475.30  2024-08-13\n",
       "3     4         20          23    5    55893.00  2023-02-03\n",
       "4     5          8          57    4   451403.90  2024-02-12\n",
       "..  ...        ...         ...  ...         ...         ...\n",
       "95   98         21         142    2     1570.35  2024-02-13\n",
       "96   99         49          81    9  1099336.00  06-01-2024\n",
       "97  100         22          93    4   381812.60  21-01-2023\n",
       "98  101         11          47    8    48984.00  04-07-2024\n",
       "99  102          9          67    9   733495.95  2024-02-02\n",
       "\n",
       "[100 rows x 6 columns]"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "vendas.head(100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "16c8b506-5e81-4c07-84ef-167454a8c609",
   "metadata": {},
   "outputs": [],
   "source": [
    "# transformando o tipo de data\n",
    "vendas[\"sale_date\"] = pd.to_datetime(\n",
    "    vendas[\"sale_date\"],\n",
    "    format=\"mixed\",\n",
    "    dayfirst=True,\n",
    "    errors=\"coerce\"\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "a533cd6d-b29b-41b1-bc4e-839a6d8c3b1b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "np.int64(0)"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "vendas[\"sale_date\"].isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "6f7d8381-883a-467c-8af4-6375a2f8a6ea",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "np.int64(0)"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "vendas.duplicated().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "cad75ee2-5d2c-475c-b62e-587fc4bfbfe4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "id                     int64\n",
       "id_client              int64\n",
       "id_product             int64\n",
       "qtd                    int64\n",
       "total                float64\n",
       "sale_date     datetime64[us]\n",
       "dtype: object"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "vendas.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "08f29239-303d-4cb2-a61c-a54314f00263",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>id_client</th>\n",
       "      <th>id_product</th>\n",
       "      <th>qtd</th>\n",
       "      <th>total</th>\n",
       "      <th>sale_date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>42</td>\n",
       "      <td>105</td>\n",
       "      <td>11</td>\n",
       "      <td>3405.0</td>\n",
       "      <td>2023-10-09</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>136</td>\n",
       "      <td>9</td>\n",
       "      <td>16873.9</td>\n",
       "      <td>2024-09-15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>25</td>\n",
       "      <td>139</td>\n",
       "      <td>7</td>\n",
       "      <td>9475.3</td>\n",
       "      <td>2024-08-13</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>20</td>\n",
       "      <td>23</td>\n",
       "      <td>5</td>\n",
       "      <td>55893.0</td>\n",
       "      <td>2023-03-02</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>8</td>\n",
       "      <td>57</td>\n",
       "      <td>4</td>\n",
       "      <td>451403.9</td>\n",
       "      <td>2024-12-02</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   id  id_client  id_product  qtd     total  sale_date\n",
       "0   0         42         105   11    3405.0 2023-10-09\n",
       "1   1          3         136    9   16873.9 2024-09-15\n",
       "2   2         25         139    7    9475.3 2024-08-13\n",
       "3   4         20          23    5   55893.0 2023-03-02\n",
       "4   5          8          57    4  451403.9 2024-12-02"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "vendas.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0397e7c0-200c-495d-acc3-8794d3f96623",
   "metadata": {},
   "source": [
    "Conclui-se que nesta base não exite nulos ou duplicatas\n",
    "## Tratamento da base de vendas - coluna de datas inconsistentes\n",
    "durante a identificação dos tipos de dados o campo sale_date estava como string\n",
    "e que possuía formatos mistos de data, incluindo padrões ISO (YYYY-MM-DD) e brasileiro (DD-MM-YYYY).\n",
    "\n",
    "Para garantir a correta interpretação, foi utilizada a conversão com\n",
    "`format=\"mixed\"` e `dayfirst=True`, permitindo o tratamento adequado\n",
    "dos diferentes formatos presentes na base.\n",
    "durante a exploração dos dados verifiquei os se existe dados nulos e ou duplicatas\n",
    "e não existem.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d318f209-35c4-49a5-9177-4414720e7f58",
   "metadata": {},
   "source": [
    "## Criando a Tabela analitica"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "33c9dae5-4cab-45d6-9e2a-4a3712f99e91",
   "metadata": {},
   "outputs": [],
   "source": [
    "#fazendo a ligação das tabelas pelo seus identificadores e criando a tabela analitica\n",
    "df_analitico = vendas.merge(produtos, left_on=\"id_product\", right_on=\"product_id\", how=\"left\")\n",
    "\n",
    "df_analitico = df_analitico.merge(clientes_crm, left_on=\"id_client\", right_on=\"client_id\", how=\"left\")\n",
    "\n",
    "df_analitico = df_analitico.merge(custo_final[[\"product_id\", \"usd_price\"]], on=\"product_id\", how=\"left\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "b8c3e48a-1e9e-4e37-8431-7760b0b2126f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>id_client</th>\n",
       "      <th>id_product</th>\n",
       "      <th>qtd</th>\n",
       "      <th>total</th>\n",
       "      <th>sale_date</th>\n",
       "      <th>name</th>\n",
       "      <th>price</th>\n",
       "      <th>product_id</th>\n",
       "      <th>actual_category</th>\n",
       "      <th>full_name</th>\n",
       "      <th>location</th>\n",
       "      <th>client_id</th>\n",
       "      <th>email</th>\n",
       "      <th>estado</th>\n",
       "      <th>cidade</th>\n",
       "      <th>usd_price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>42</td>\n",
       "      <td>105</td>\n",
       "      <td>11</td>\n",
       "      <td>3405.0</td>\n",
       "      <td>2023-10-09</td>\n",
       "      <td>Cabo de Nylon Danforth Prime</td>\n",
       "      <td>309.54</td>\n",
       "      <td>105</td>\n",
       "      <td>ancoragem</td>\n",
       "      <td>Márcia Figueiredo</td>\n",
       "      <td>Vila do Conde (Barcarena) - PA</td>\n",
       "      <td>42</td>\n",
       "      <td>márcia.figueiredo#protonmail.com</td>\n",
       "      <td>PA</td>\n",
       "      <td>Vila do Conde Barcarena</td>\n",
       "      <td>53.37</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>136</td>\n",
       "      <td>9</td>\n",
       "      <td>16873.9</td>\n",
       "      <td>2024-09-15</td>\n",
       "      <td>Cabo de Nylon Bruce Flux Hydro</td>\n",
       "      <td>1973.50</td>\n",
       "      <td>136</td>\n",
       "      <td>ancoragem</td>\n",
       "      <td>Daniel Farias Ribeiro Teixeira</td>\n",
       "      <td>Rio Grande,RS</td>\n",
       "      <td>3</td>\n",
       "      <td>farias.teixeira.daniel.ribeiro#gmail.com</td>\n",
       "      <td>RS</td>\n",
       "      <td>Rio Grande</td>\n",
       "      <td>390.62</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   id  id_client  id_product  qtd    total  sale_date  \\\n",
       "0   0         42         105   11   3405.0 2023-10-09   \n",
       "1   1          3         136    9  16873.9 2024-09-15   \n",
       "\n",
       "                             name    price  product_id actual_category  \\\n",
       "0    Cabo de Nylon Danforth Prime   309.54         105       ancoragem   \n",
       "1  Cabo de Nylon Bruce Flux Hydro  1973.50         136       ancoragem   \n",
       "\n",
       "                        full_name                        location  client_id  \\\n",
       "0               Márcia Figueiredo  Vila do Conde (Barcarena) - PA         42   \n",
       "1  Daniel Farias Ribeiro Teixeira                   Rio Grande,RS          3   \n",
       "\n",
       "                                      email estado                   cidade  \\\n",
       "0          márcia.figueiredo#protonmail.com     PA  Vila do Conde Barcarena   \n",
       "1  farias.teixeira.daniel.ribeiro#gmail.com     RS               Rio Grande   \n",
       "\n",
       "   usd_price  \n",
       "0      53.37  \n",
       "1     390.62  "
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_analitico.head(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "193937b4-10b1-46ee-95a0-1ba11bf5ce5a",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_analitico = df_analitico.drop(columns=[\"product_id\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "280345ba-83dc-4f32-b59d-4d1d25cd6188",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(10364, 16)"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_analitico.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "27f358b0-1613-4dfa-9e24-5ed636f89079",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "id                 0\n",
       "id_client          0\n",
       "id_product         0\n",
       "qtd                0\n",
       "total              0\n",
       "sale_date          0\n",
       "name               0\n",
       "price              0\n",
       "actual_category    0\n",
       "full_name          0\n",
       "location           0\n",
       "client_id          0\n",
       "email              0\n",
       "estado             0\n",
       "cidade             0\n",
       "usd_price          0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_analitico.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "876ee3bc-47d5-437d-abc9-5d11161a70e5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>id_client</th>\n",
       "      <th>id_product</th>\n",
       "      <th>qtd</th>\n",
       "      <th>total</th>\n",
       "      <th>sale_date</th>\n",
       "      <th>name</th>\n",
       "      <th>price</th>\n",
       "      <th>actual_category</th>\n",
       "      <th>full_name</th>\n",
       "      <th>location</th>\n",
       "      <th>client_id</th>\n",
       "      <th>email</th>\n",
       "      <th>estado</th>\n",
       "      <th>cidade</th>\n",
       "      <th>usd_price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>42</td>\n",
       "      <td>105</td>\n",
       "      <td>11</td>\n",
       "      <td>3405.0</td>\n",
       "      <td>2023-10-09</td>\n",
       "      <td>Cabo de Nylon Danforth Prime</td>\n",
       "      <td>309.54</td>\n",
       "      <td>ancoragem</td>\n",
       "      <td>Márcia Figueiredo</td>\n",
       "      <td>Vila do Conde (Barcarena) - PA</td>\n",
       "      <td>42</td>\n",
       "      <td>márcia.figueiredo#protonmail.com</td>\n",
       "      <td>PA</td>\n",
       "      <td>Vila do Conde Barcarena</td>\n",
       "      <td>53.37</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>136</td>\n",
       "      <td>9</td>\n",
       "      <td>16873.9</td>\n",
       "      <td>2024-09-15</td>\n",
       "      <td>Cabo de Nylon Bruce Flux Hydro</td>\n",
       "      <td>1973.50</td>\n",
       "      <td>ancoragem</td>\n",
       "      <td>Daniel Farias Ribeiro Teixeira</td>\n",
       "      <td>Rio Grande,RS</td>\n",
       "      <td>3</td>\n",
       "      <td>farias.teixeira.daniel.ribeiro#gmail.com</td>\n",
       "      <td>RS</td>\n",
       "      <td>Rio Grande</td>\n",
       "      <td>390.62</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>25</td>\n",
       "      <td>139</td>\n",
       "      <td>7</td>\n",
       "      <td>9475.3</td>\n",
       "      <td>2024-08-13</td>\n",
       "      <td>Boia de Arqueamento Danforth Torque</td>\n",
       "      <td>1424.88</td>\n",
       "      <td>ancoragem</td>\n",
       "      <td>Femininos Antunes Lopes Ribeiro Amaral</td>\n",
       "      <td>ES / São Mateus</td>\n",
       "      <td>25</td>\n",
       "      <td>femininos.antunes.amaral.lopes.ribeiro@icloud.com</td>\n",
       "      <td>ES</td>\n",
       "      <td>São Mateus</td>\n",
       "      <td>246.89</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>20</td>\n",
       "      <td>23</td>\n",
       "      <td>5</td>\n",
       "      <td>55893.0</td>\n",
       "      <td>2023-03-02</td>\n",
       "      <td>Piloto Automático Furuno Torque Peak</td>\n",
       "      <td>11178.63</td>\n",
       "      <td>eletrônicos</td>\n",
       "      <td>Bruno Silva</td>\n",
       "      <td>PA , Santarém Novo</td>\n",
       "      <td>20</td>\n",
       "      <td>silva.bruno@zoho.com</td>\n",
       "      <td>PA</td>\n",
       "      <td>Santarém Novo</td>\n",
       "      <td>2244.66</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>8</td>\n",
       "      <td>57</td>\n",
       "      <td>4</td>\n",
       "      <td>451403.9</td>\n",
       "      <td>2024-12-02</td>\n",
       "      <td>Motor de Popa Honda Vector Kinetic 174HP</td>\n",
       "      <td>118790.57</td>\n",
       "      <td>propulsão</td>\n",
       "      <td>Luiz Alves Pimentel</td>\n",
       "      <td>SE - Aracaju</td>\n",
       "      <td>8</td>\n",
       "      <td>pimentel.alves.luiz#outlook.com</td>\n",
       "      <td>SE</td>\n",
       "      <td>Aracaju</td>\n",
       "      <td>20486.78</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   id  id_client  id_product  qtd     total  sale_date  \\\n",
       "0   0         42         105   11    3405.0 2023-10-09   \n",
       "1   1          3         136    9   16873.9 2024-09-15   \n",
       "2   2         25         139    7    9475.3 2024-08-13   \n",
       "3   4         20          23    5   55893.0 2023-03-02   \n",
       "4   5          8          57    4  451403.9 2024-12-02   \n",
       "\n",
       "                                       name      price actual_category  \\\n",
       "0              Cabo de Nylon Danforth Prime     309.54       ancoragem   \n",
       "1            Cabo de Nylon Bruce Flux Hydro    1973.50       ancoragem   \n",
       "2       Boia de Arqueamento Danforth Torque    1424.88       ancoragem   \n",
       "3      Piloto Automático Furuno Torque Peak   11178.63     eletrônicos   \n",
       "4  Motor de Popa Honda Vector Kinetic 174HP  118790.57       propulsão   \n",
       "\n",
       "                                full_name                        location  \\\n",
       "0                       Márcia Figueiredo  Vila do Conde (Barcarena) - PA   \n",
       "1          Daniel Farias Ribeiro Teixeira                   Rio Grande,RS   \n",
       "2  Femininos Antunes Lopes Ribeiro Amaral                 ES / São Mateus   \n",
       "3                             Bruno Silva              PA , Santarém Novo   \n",
       "4                     Luiz Alves Pimentel                    SE - Aracaju   \n",
       "\n",
       "   client_id                                              email estado  \\\n",
       "0         42                   márcia.figueiredo#protonmail.com     PA   \n",
       "1          3           farias.teixeira.daniel.ribeiro#gmail.com     RS   \n",
       "2         25  femininos.antunes.amaral.lopes.ribeiro@icloud.com     ES   \n",
       "3         20                               silva.bruno@zoho.com     PA   \n",
       "4          8                    pimentel.alves.luiz#outlook.com     SE   \n",
       "\n",
       "                    cidade  usd_price  \n",
       "0  Vila do Conde Barcarena      53.37  \n",
       "1               Rio Grande     390.62  \n",
       "2               São Mateus     246.89  \n",
       "3            Santarém Novo    2244.66  \n",
       "4                  Aracaju   20486.78  "
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_analitico.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "df63e580-e661-4da8-bc42-6099297a6b74",
   "metadata": {},
   "source": [
    "## Validação da base integrada\n",
    "\n",
    "Após a junção das tabelas, foi realizada a validação da base final,\n",
    "verificando a quantidade de registros e possíveis valores nulos\n",
    "gerados durante o processo de merge.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6c67ddbf-0eed-4d49-a7f1-1b00f25b462e",
   "metadata": {},
   "source": [
    "## Criando as métricas\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "284ea568-0acb-4e74-8324-644b1843c810",
   "metadata": {},
   "outputs": [],
   "source": [
    "cambio_anual = {2023: 4.99, 2024: 5.39}  # câmbio médio anual BCB"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "3178dcc4-0f4d-4dda-83fd-96dd22d9725e",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_analitico['ano']            = df_analitico['sale_date'].dt.year\n",
    "df_analitico['cambio']         = df_analitico['ano'].map(cambio_anual)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "87ac47b3-6845-450b-841b-f400a6815030",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_analitico[\"preco_unitario\"] = df_analitico[\"total\"] / df_analitico[\"qtd\"]\n",
    "df_analitico['custo_brl']      = df_analitico[\"usd_price\"] * df_analitico[\"cambio\"]\n",
    "df_analitico[\"lucro_unitario\"] = df_analitico[\"preco_unitario\"] - df_analitico[\"custo_brl\"]\n",
    "df_analitico[\"lucro_total\"] = df_analitico[\"lucro_unitario\"] * df_analitico[\"qtd\"]\n",
    "df_analitico[\"margem_pct\"] = (df_analitico[\"lucro_unitario\"] / df_analitico[\"preco_unitario\"]) * 100\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "048354ea-fa77-4e0f-a45e-69c489cafd75",
   "metadata": {},
   "source": [
    "Foram criadas métricas derivadas para análise de performance:\n",
    "foi criado também o cambio anual, para aplicar em custo_brl\n",
    "\n",
    "- Preço unitário\n",
    "- Lucro unitário\n",
    "- Lucro total\n",
    "- Margem por porcetagem\n",
    "\n",
    "Essas métricas permitem avaliar a rentabilidade das operações."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "3a07af43-543e-4c97-8ade-c01368b1719f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "id                          int64\n",
       "id_client                   int64\n",
       "id_product                  int64\n",
       "qtd                         int64\n",
       "total                     float64\n",
       "sale_date          datetime64[us]\n",
       "name                          str\n",
       "price                     float64\n",
       "actual_category               str\n",
       "full_name                     str\n",
       "location                      str\n",
       "client_id                   int64\n",
       "email                         str\n",
       "estado                        str\n",
       "cidade                        str\n",
       "usd_price                 float64\n",
       "ano                         int32\n",
       "cambio                    float64\n",
       "preco_unitario            float64\n",
       "custo_brl                 float64\n",
       "lucro_unitario            float64\n",
       "lucro_total               float64\n",
       "margem_pct                float64\n",
       "dtype: object"
      ]
     },
     "execution_count": 65,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_analitico.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "cb83fd58-62d6-4585-b68d-add4042865a9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>id_client</th>\n",
       "      <th>id_product</th>\n",
       "      <th>qtd</th>\n",
       "      <th>total</th>\n",
       "      <th>sale_date</th>\n",
       "      <th>name</th>\n",
       "      <th>price</th>\n",
       "      <th>actual_category</th>\n",
       "      <th>full_name</th>\n",
       "      <th>...</th>\n",
       "      <th>estado</th>\n",
       "      <th>cidade</th>\n",
       "      <th>usd_price</th>\n",
       "      <th>ano</th>\n",
       "      <th>cambio</th>\n",
       "      <th>preco_unitario</th>\n",
       "      <th>custo_brl</th>\n",
       "      <th>lucro_unitario</th>\n",
       "      <th>lucro_total</th>\n",
       "      <th>margem_pct</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>42</td>\n",
       "      <td>105</td>\n",
       "      <td>11</td>\n",
       "      <td>3405.0</td>\n",
       "      <td>2023-10-09</td>\n",
       "      <td>Cabo de Nylon Danforth Prime</td>\n",
       "      <td>309.54</td>\n",
       "      <td>ancoragem</td>\n",
       "      <td>Márcia Figueiredo</td>\n",
       "      <td>...</td>\n",
       "      <td>PA</td>\n",
       "      <td>Vila do Conde Barcarena</td>\n",
       "      <td>53.37</td>\n",
       "      <td>2023</td>\n",
       "      <td>4.99</td>\n",
       "      <td>309.545455</td>\n",
       "      <td>266.3163</td>\n",
       "      <td>43.229155</td>\n",
       "      <td>475.5207</td>\n",
       "      <td>13.965366</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>136</td>\n",
       "      <td>9</td>\n",
       "      <td>16873.9</td>\n",
       "      <td>2024-09-15</td>\n",
       "      <td>Cabo de Nylon Bruce Flux Hydro</td>\n",
       "      <td>1973.50</td>\n",
       "      <td>ancoragem</td>\n",
       "      <td>Daniel Farias Ribeiro Teixeira</td>\n",
       "      <td>...</td>\n",
       "      <td>RS</td>\n",
       "      <td>Rio Grande</td>\n",
       "      <td>390.62</td>\n",
       "      <td>2024</td>\n",
       "      <td>5.39</td>\n",
       "      <td>1874.877778</td>\n",
       "      <td>2105.4418</td>\n",
       "      <td>-230.564022</td>\n",
       "      <td>-2075.0762</td>\n",
       "      <td>-12.297549</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>2 rows × 23 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   id  id_client  id_product  qtd    total  sale_date  \\\n",
       "0   0         42         105   11   3405.0 2023-10-09   \n",
       "1   1          3         136    9  16873.9 2024-09-15   \n",
       "\n",
       "                             name    price actual_category  \\\n",
       "0    Cabo de Nylon Danforth Prime   309.54       ancoragem   \n",
       "1  Cabo de Nylon Bruce Flux Hydro  1973.50       ancoragem   \n",
       "\n",
       "                        full_name  ... estado                   cidade  \\\n",
       "0               Márcia Figueiredo  ...     PA  Vila do Conde Barcarena   \n",
       "1  Daniel Farias Ribeiro Teixeira  ...     RS               Rio Grande   \n",
       "\n",
       "  usd_price   ano cambio  preco_unitario  custo_brl  lucro_unitario  \\\n",
       "0     53.37  2023   4.99      309.545455   266.3163       43.229155   \n",
       "1    390.62  2024   5.39     1874.877778  2105.4418     -230.564022   \n",
       "\n",
       "   lucro_total  margem_pct  \n",
       "0     475.5207   13.965366  \n",
       "1   -2075.0762  -12.297549  \n",
       "\n",
       "[2 rows x 23 columns]"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_analitico.head(2)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1ab7faaf-be4c-4c1c-a965-2eb2593978ee",
   "metadata": {},
   "source": [
    "## analises"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "722fc40a-fec8-4af9-bc81-e06e41b32199",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "name\n",
       "Motor Diesel Yanmar Velocity 37HP             -8.572839e+06\n",
       "Motor Elétrico Tohatsu Zenith Oceanic 113HP   -5.929223e+06\n",
       "Name: lucro_total, dtype: float64"
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#produtos com prejuizo\n",
    "df_analitico.groupby(\"name\")[\"lucro_total\"].sum().sort_values().head(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "a2cbf349-2fa6-4467-a110-ef7c38bcb0bf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "name\n",
       "Motor Diesel Parsun Velocity Abyss Orca 235HP           6.898966e+06\n",
       "Motor Elétrico Honda Flux Ultra 273HP                   6.709743e+06\n",
       "Motor de Popa Volvo Hydro Dash 256HP                    6.073140e+06\n",
       "Motor Diesel Yanmar Hydro Magnum Boost 267HP            4.649250e+06\n",
       "Motor Elétrico Torqeedo Pulse 300HP                     4.121668e+06\n",
       "Motor Elétrico Yamaha Swift Drift Current 265HP         3.527640e+06\n",
       "Motor Elétrico Torqeedo Ion Orca Vox 186HP              3.483965e+06\n",
       "Motor Elétrico Torqeedo Barracuda Magnum Helix 101HP    3.479741e+06\n",
       "Motor de Popa Honda Vector Kinetic 174HP                3.150987e+06\n",
       "Motor de Popa Parsun Impulse 162HP                      2.852303e+06\n",
       "Name: lucro_total, dtype: float64"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "top_produtos = df_analitico.groupby(\"name\")[\"lucro_total\"].sum().sort_values(ascending=False)\n",
    "top_produtos.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "993473fb-4612-4136-8893-96a9b319719b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "79d46684-b8c7-433f-b467-597f5b34cd20",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "id_client\n",
       "15    1.960191e+06\n",
       "1     1.866650e+06\n",
       "25    1.833569e+06\n",
       "5     1.825141e+06\n",
       "45    1.695134e+06\n",
       "2     1.618571e+06\n",
       "9     1.583044e+06\n",
       "49    1.558440e+06\n",
       "27    1.490994e+06\n",
       "26    1.476740e+06\n",
       "Name: lucro_total, dtype: float64"
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# clientes mais importantes\n",
    "df_analitico.groupby(\"id_client\")[\"lucro_total\"].sum().sort_values(ascending=False).head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "61812999-e392-4f70-99ab-6ef49a86cba3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "actual_category\n",
       "ancoragem      1.821968e+06\n",
       "eletrônicos    1.110472e+07\n",
       "propulsão      3.517711e+07\n",
       "Name: lucro_total, dtype: float64"
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#categorias\n",
    "df_analitico.groupby(\"actual_category\")[\"lucro_total\"].sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c180b8dc-8928-4ba7-b137-398ebbda91fe",
   "metadata": {},
   "source": [
    "## Vizualização"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "d8807db5-e51d-4981-94bf-1d6a06b7fc3a",
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.rcParams.update({\n",
    "    \"figure.facecolor\": \"white\",\n",
    "    \"axes.facecolor\":   \"white\",\n",
    "    \"axes.spines.top\":  False,\n",
    "    \"axes.spines.right\":False,\n",
    "    \"axes.titlesize\":   13,\n",
    "    \"axes.titleweight\": \"bold\",\n",
    "    \"axes.labelsize\":   11,\n",
    "    \"xtick.labelsize\":  10,\n",
    "    \"ytick.labelsize\":  10,\n",
    "})\n",
    "\n",
    "COR_LUCRO  = \"#1D9E75\"\n",
    "COR_PREJ   = \"#D85A30\"\n",
    "COR_NEUTRA = \"#185FA5\"\n",
    "\n",
    "def fmt_milhoes(x, _):\n",
    "    return f\"R$ {x:.1f}M\"\n",
    "\n",
    "def fmt_brl(valor):\n",
    "    return f\"R$ {valor:,.0f}\".replace(\",\", \".\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b3229f69-68e0-486e-8a67-e07e3a974c7b",
   "metadata": {},
   "source": [
    "## Análise 1 — Top produtos por lucro e produtos com prejuízo\n",
    "\n",
    "Comparativo direto entre os produtos mais rentáveis e os que precisam de atenção."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "2a81231d-835a-40a3-b71c-062b45c0ebab",
   "metadata": {
    "jupyter": {
     "source_hidden": true
    }
   },
   "outputs": [
    {
     "data": {
      "image/png": "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7eLacv/9739bk3ishV7tWnNc6+3ggw+OPx900EFtAstGlvlk6YW0/EK+DANLNXABa9BJ5fpx2HnnncPGG28cfz766KNjgo7tYx33fCYan6ErkEBiW0jiMfuNpSxZboLk3P7779/6OC6QzTKYfK7JJ588Xkgb6623XjjkkEPisqXMQKyG4CAl2fjeuNGR5ULc1eTJTKr/mNVI9R/LeLIPmz0W+O75DCTfJphggrgUKzP9ko5cu29Q43Odd955rcvREhjVwneUkp/MYuT6BgQZBxxwQFPvu9FGG4WTTz45BkdcY3DTTTeNxwzXTuCaAskmm2wSOhvBUaVrL44//vjx2nwcU3lClm1gORSWQ2XpkyKurcgxwPUcwLIxBHAEfAR+DzzwQJhlllnCtttu2+33jSRJUtkZ+3U+Yz9jv7LHN1ybkMtiPPfcc3FMYPHFF4+xI0tiMkuvX79+8bqAFBbff//9NV+r2XizGsYZWLEpFU1POOGEcZwoL0ImVmXbm/0bldqlRZKkLnLwwQcz7SbeJplkkjb3ffnlly1TTTVV6/3F24gjjthy7733tj7+oYcear1v9NFHj69XfM6www7b8sADDzS9bdVuG2+8cZvnrL/++lUfO8sss7T88MMPDb33IossUvU9GnnORRddVPExV111VdwH1bZxjjnmaOnfv3/r4++6666WYYYZZqDHTTPNNG3+369fv9bnXHHFFRVfe8YZZ6z6XZ9zzjkVn3PZZZe161hYeumla35vO+20U0t3kB+jZ511VsPHI991/h1V+oyLLrpom/8nfFeVfo/jjz++pVevXlX323LLLdfy559/NnXMNfJ5av3NJEsuueRA9w833HAtU089dev/ec3ku+++a5l55pmrvvZJJ51U8XvgPFJJs/tGkiRJ1ft/xn7/x9jP2G9Iiv2Kf/uNPKfamMi7777bMuGEE9aMKfP9x3ZX+n174s1K21fc3/W2p9nxGalZLvUpSeqWWOv9+eefD4ceemiYddZZw4gjjhhngTEbbPPNN4/XbuNiyZWMMsoocTlKqqOYQcW18VhKgkovKsEGlUsvvTRceOGFYb755gsjjzxyfN/pp58+zjxkiQiWBO1K66yzTnj22WfjfqESjtlhbCdLiB533HFxG1lKIllmmWXC3XffHeadd94484yZeVS/Pfroo1Xfg5mBXHuAa+zx+sywPPHEE8Mpp5xS9Tl8n1S7URFXXAKjPccCM7mYXcnyGVQQs+wjlXV8DrajO17fr734jm644Ya4X1jihFmozHA999xzm36tPfbYIzz00EPxYu3scyoL2W8sM3vOOefE5Vr5TrsCf1tURXJ88v0vscQS8Tjkb60SjlUqKzn2eAyfg21nmRRmhs4zzzyl2TeSJEk9nbFf5zP2M/Yre3zDWAMzFol/WS2HsQ3GLYiJufTHkUceGS//0cjyoc3Gm13xNyo1qxfZv6afJUlSN/Pwww+HxRZbLP5M0oklGiRJkiRJ5WLsJ6lZp512WlwOFCT5rrnmGneiSs1FYiVJkiRJkiRJUqn8+eef4auvvgrXXntt6+9YmUkqO5f6lCRJkiRJkiRJpXLUUUfFVaFYOjNdGobLg0hlZ+JPkiRJkiRJkiSVUu/eveO1/+69994w9thjd/XmSIOc1/iTJEmSJEmSJEmSSsAZf5IkSZIkSZIkSVIJmPiTJEmSJEmSJEmSSsDEnyRJkiRJkiRJklQCJv4kdUstLS1hwIAB8V9JkiRJkowZJUmS6jPxJ6lb+umnn0Lfvn3jv5IkSZIkGTNKkiTVZ+JPkiRJkiRJkiRJKgETf5IkSZIkSZIkSVIJmPiTJEmSJEmSJEmSSsDEnyRJkiRJkiRJklQCJv4kSZIkSZIkSZKkEjDxJ0mSJEmSJEmSJJWAiT9JkiRJkiRJkiSpBEz8SZIkSZIkSZIkSSVg4k+SJEmSJEmSJEkqARN/kiRJkiRJkiRJUgmY+JMkSZIkSZIkSZJKwMSfJEmSJEmSJEmSVAIm/iRJkiRJkiRJkqQSMPEnSZIkSZIkSZIklYCJP0mSJEmSJEmSJKkETPxJkiRJkiRJkiRJJWDiT5IkSZIkSZIkSSoBE3+SJEmSJEmSJElSCZj4kyRJkiRJkiRJkkrAxJ8kSZIkSZIkSZJUAib+JEmSJEmSJEmSpBIw8SdJkiRJkiRJkiSVwDBdvQGSVMv0lx8Yhuo9vDtJkiS1+mTT49wbkqTB5p31Z3NvS5KkgUxzxUuhO3LGnyRJkiRJkiRJklQCJv4kSZIkSZIkSZKkEjDxJ0mSJEmSJEmSJJWAiT9JkiRJkiRJkiSpBEz8SZIkSZIkSZIkSSVg4k+SJEmSJEmSJEkqARN/kiRJkoYom2yySVdvgiQNVp73JEmShhwm/rrYxRdfHEYdddTSvl9P99FHH4VevXqFl19+uVu+XnuCvVVWWaVL3luSJGlQWnTRRcPwww8fRh555DD66KOHRRZZJDz//PMdes2WlpZw9NFHh0knnTSMNNJIYeqppw7PPPNM1cffcsstYeaZZw59+vQJk002WTjppJPa3H/VVVeF6aabLm7jXHPNFZ577rk2959//vnxPUYZZZQw7bTThiuvvLLm9p188slh8sknj6+3+OKLh/fff7/N/Z999llYc801Y/+f29JLL93m/jfffDP+jvdjn22++eZN7B11BePHnmdQxpSD4rxX9Pfff4dddtkljD/++KFv375hwQUXDC+88ELNY3TooYeO25Ruxx13XOv9yy67bJv7RhhhhDDUUEOF7777Lt5/wgkntJ5HJ5xwwrDHHnuEP//8s+Y2brPNNmHssceO+2CZZZYJH3zwQet9nMM5T/J64447boyJf/zxx9b7eSzbNNpoo4UJJpigzbZKkiT1VD0i8UfHjI4tnbmi7bffPt7XTPXaww8/HJ+Td/Y6G6+fbgwSTDXVVHEbix3ktddeO7z77ruhO8m3nY79AgssEB588MHQkxAYjDnmmOGYY46peP/hhx8exhlnnPDXX38N1u2aaKKJwpdffhlmnHHGQXYsbr311jHQuu666zrtNSVJknqCY489Nvz888/hq6++CvPMM09YbbXV2tx/6aWXxsQbCTgGiRkk/+GHH6q+3v777x/uuOOOcP/998fXve+++8LEE09c8bHffPNNWGuttcLee+8d+vfvH26++eZw6KGHhnvuuSfe/8QTT8R4hkFx7t9iiy3CcsstF3/GSy+9FLbbbrtwzjnnhAEDBoQzzjgjbLbZZjE5Vwmf4b///W+4884742eYf/75w4orrhj++eefeP8vv/wSFltssTDLLLOETz/9NA6qH3HEEa3P/+KLL2KykG1m2+mjEluVgfHj4EEcO+KIIw6UoP7333/j8bjGGmuEnqynxJRbbrll/Ht/++23O3zeW2mlleI5jmTceOONFzbccMNw5JFHhttuuy089dRTYeedd47nsjnnnHOgMY+Ec99www0Xz5npttdee7UmLEnE8bvXX389bvcff/wRiyymmWaasNRSS8Xz1QUXXBC+//778PTTT8eY+ZBDDqm5T9577714rmS/UKixwQYbtN7Hccj5lfMqxyzfK8lEcL7kM88+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n6oDbJIkSbljjz02Dtx99dVXYZ555gmrrbZam/svvfTSmFgjwTb22GPHgcYffvih6k7cf//9wx133BHuv//++Lr33XdfmHjiiSs+lgE8HpNujzzySBhqqKHCmmuuGe//66+/woorrhiWWGKJ8L///S8mBNdbb73w/vvvx/sZ0CN+YaCyf//+YYsttgjLLbdc/LmS/fbbr8378dkY/GPQMffFF1+E448/Pib5cvTV7r333vj5GYCkP8YgYxkZH3av+DB9H9Vuxbh2cCdOO8tHH31U83OSOOhMFApstdVW7fq+6/nnn3/CSSedFM8jI4wwQozTONfkiQipq9vsSjhm87Zyr732qvrY3XffPXz44YfhzTffjH+/tJ95kQHHPudGxlwonjnnnHNiYU36G1lppZXC7LPPHtvUBx98MJx++unhyiuvrPhebAvJPgo1eL3DDjssrLvuuvG9we/4G6Mgh3E/zpv0Cb777rt4P3+DnMe+/fbb2E8488wzwwYbbBD69evX1P6RJKlHJf4w0UQTxaTZb7/91vq733//PTa61YL1QY2K4VoJoosuuih8+eWXbW71EjVU97zxxhuxc9Eef/75Z/yXCiuqllTflltuOdD3NMwww5Rm1zEo1R5PPvlkmHnmmcMNN9wQXn311Vgdt9FGG4Xbb7+99TF0kvP99vrrr8cKvDQgBqrf6SDTwX388cdj4L/UUkvFDq0kSVIjhhtuuLDxxhuHTz/9tLUP8fnnn4fNNtssJtwYXPv444/DAQccULUfl5JzF154YZhyyinjIPokk0wSi5waccEFF8Q+DHEJHn300Th4d+CBB8bBwxVWWCEOYl522WXx/ltuuSUWUTH4Sf9o6623jrMTGq3g5/34XL179x6o8JH3pL+f43Okz0Kcwnsy0NnevmB3Z3zYfeLDU045pU1MUIyFa8107WnHXDFu5HbbbbfFvzf+NjvTWGONFWcTdzbOD+uss05MTOy8885x5jJFn3w+Cjs7K7moIVdntNmdgfZ2n332iUk1CgMosKGNTuOKFEPMMMMM8e+XYmUSlYxZ4J133om3gw8+OAw77LBxZiBF+ikxWDT55JOHPfbYI874o0iIwiCeQyIQc889d0zk83fN+zEOxb+MtSCtQsBz+RvlX5KPtOOSJJU68UcijI5ovtQNP5P0o6om98cff8SlUKggIghfcMEF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N910U9X3+vLLL8NKK60Uxh9//Lr9+P322y8+5uabb27z+3POOSdMPPHE8bMtv/zy8TWlQe3iiy8Oo446aqnerzvEi91hG3pCO7HLLrt09WZI6iH9wFrWW2+9uv2vPffcM0wzzTRhlFFGCZNNNlnsUxbRV6TPR1+MPt3ZZ5890GO+/vrr+Jl4XDXvvvtuWHXVVcO4444b2zz6o0888UTD/VD88ccfYY899gjjjTdevH+mmWaK48WSNMQm/kiocLLcZpttBrpv++23j/c1U03SUzvsabvTbZxxxgmrr756+PDDD7tsm2gchx122HD11VdXvH/zzTcPs88+e+juydfuHKDk3/tQQw0VB6pmm222sNdee3WLwSM6VnPNNVfsaI099tgx+fnOO+8MtH/zY7fa3zODBjPPPHMYYYQR4mvx993I360JS0mSBo9jjz02/Pzzz+Grr74K88wzT1httdXa3H/ppZeG6aabLlx11VWxLWdQ6Icffqj6evvvv3+44447wv333x9f97777ouJskr++uuvsOKKK4Ylllgi/O9//4sDKQwKvf/++/H+9ddfP75Guj3yyCOx77TmmmvG+0cbbbTY1/j2229D//79w5lnnhk22GCD0K9fv4rvx3OXWWaZgZJ5Ra+88kq47bbb4iBO7sEHHwx77713uO6668I333wT++5so7qHnhhj5n1pBjCnmmqquI0vvPBCm8etvfbacYCyO+iJ8WLxxnmiK91+++3xXEq8RdEDsRfnsu7oxhtvDIcffni7nss5nnMmA+FpgH6jjTYKX3zxxUCxX/E7OuaYY9o85tprr40D+OyvSSaZJBx//PEd+lySBk0/sBr6hrQf9TB2xHmHtveuu+6KBVfnnntu6/1333132G677WKB+4ABA8Ibb7wRx6eKdthhhzjOVgvvseyyy4bXXnstfP/997H9XW655cJ3333XUD8Um266afjggw9iu/3TTz/FPuLgLNSRpG4542+iiSaKwcJvv/3W+rvff/89XHnllVUHBwY1KpT//vvvwf6+JFXo/NJA0GgxAPLPP/+ErsAABtXLF1544UD3/fLLL7HDTTCnEP78889O+d6fe+65GBAxQDbjjDPGTkdXojPD4MjTTz8dB+sI2JZaaqn4/ee23HLLmKhMt+OOO67N/QzeMfi3zz77xOOaz7f00ksP5k8jSZIaMdxw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xJ8kSZIkSZIkSZJUAib+JEmSJEmSJEmSpBIw8SdJkiRJkiRJkiSVgIk/SZIkSZIkSZIkqQRM/HWRm2++OVx11VVd9faSJKmH2mSTTbp6EyRJkiSpxzGWkjSkMPE3iFx88cVh1FFHrXjf008/HXbaaacw33zztfv1F1100bDLLrt0YAuHHLW+i8HJ70ySVKuNGH744cPII48cRh999LDIIouE559/vlN22Ouvvx6GG264sMoqq1R9zJ9//hnWWGONMOmkk4ZevXrFAqXcHXfcERZeeOEw2mijhbHHHjs+9rPPPmvzHksvvXQYc8wx4/N//PHHutv15ptvxueMMsoo8TNvvvnmbe5/4oknwgILLBD3Ce950EEHtd73+eefx88zxhhjxPdca621wrffftvknpGkweujjz6K58iXX37ZXZ855JBDwqyzzuo+6SED5nl/oqWlJWy11VaxHffYllTGWCq56KKLwjTTTBP69u0b44/VVlstfPLJJ1Ufv+eee8bHE+tMNtlk4eijjx7ofEqMxjan21NPPdXmMbfeemtsH0caaaQw/vjjh7PPPruhfZBuX3zxRZvYa4kllojx3LjjjhvP3b/++mvr/cR34403XujTp0/c3iOOOKKde0pSd9EtEn+c7OgkbrPNNgPdt/3228f7mqnIePjhhxsedGovXr/S7eqrr675vO+//z4ObDGgxuBa8TWLA23V3HjjjeHwww8Pg/L7qHYrbveQEoymzz/MMMPEfbDrrruGn3/+OXSnbZx22mljh4CG/D//+U945pln2jzmf//7X1h//fVjQ04ylGOx+BleffXVsNBCC4URRhghTDTRROG4445rKDAvDmSk/6cbg7NLLbVUeOmllwbJ55eknu7YY4+N5+SvvvoqzDPPPDGYzF166aVhuummiysGkAgjoP3hhx9qvua///4bttxyy5hAq2fBBRcMl112WZhwwgkHuq9///5h7733Dp9++mno169fbEdItiXDDjts/D/FNo0gCF188cXjc7755pvw5Zdfxj5f3hatuuqqMWCm7eI9CUaT9NiPP/443vf777/HoipJ5dUTY8ZBIW13uo0zzjhh9dVXDx9++GGXbRPn/lrxIzdigzIkVYv7v3fv3mGGGWYI5557bujKBFw1FMVsu+22YeKJJ44Dwgz2UnRDcU17nHLKKW3a+rvvvjv+//bbb49t+YwzztjwuMaRRx4Z5p9//jDiiCN2i0JdST3boIilcsQunDuJiyiAnGKKKcJmm21W9fGMqTF2Sz/jrrvuCuecc85AbcV2220Xtznd8gkinF+5/+STTw4DBgwIb7zxRkzuNbIP0o1kYbLeeuvFROTXX38dXnvttfDKK6+0GVc++OCDY1vKez3yyCPhyiuvDJdffnnD+0dS99MtEn8gwUDS7Lfffmv9HYM4nGjopHYFqtf+/vvvmtUedG7zW73ON8kPTtazzz57u7aJinxQwULVyKBAZz7/TMXP+txzz7Vrm3s6Ajo+Pw0hjSkN9u677x66i6mnnjqcfvrpsQF//PHHY3KSRFs+A4KkH8fffffdF4OzRx99NFb5JDTwPGeSSSYJL7zwQjj++ONjoq8jgez9998f99s999wTOx7LLrtsjxtgkaTBicrPjTfeOCbZ0jmcGW4ElieeeGJYd911Y8LrgAMOiMUotZx66qkxwCWwrfeerCRA4cfQQw890P0Eissvv3ysHKXAhMdSXJL6SQSRFJMw4NeIk046KQbPPIdBUwYj874RQegWW2wR+1VsG+8588wzt97PADdJQ7aH/tDaa68d2z9J5dYTY8ZB5Z133olFFNddd13s36+44orhn3/+CV2Bc3AePzJwSdFJ/ju+uzJh//O5mEGx9dZbx+TaAw88ELobksIUXl5yySXh3XffjbNHGDimILk9mOmSJ+k++OCDOEOEBB5JxXr9kuI4wZprrhn3nSR1x1gqxzgZM/1S2z/UUEOF9957r+rjiWcYRyS2okifRCRjdY068MAD44onnLN5DQr8eZ32In7aYIMN4v4Za6yxwkorrdQmfpppppliTAYKOOp9PkndX7dJ/DHYQzBANUTCzwRws802W5vH/vHHH7GqmwoNKiioUE/JKJIyiy22WPyZk2Je+VnreXn1HpUYc8wxRzzh1Top0+Glc5vfeN1qbrnllvg5eczkk08eDj300NYgMc2io7o9n1WXZledf/75cap1ev3ispF8Nirx2Yds95RTThkuuOCC1vup1ph77rnjfXTM99lnn6oBKp35/DMVPyvBTa3XYtt22GGHuH00ilQU4s4774zJKQb4+I5SZWieBGJ/M+jIY/gsfF+//PJLm8+5xx57hAkmmCAOAlLFw/eW43U5bqgcZH9WCmrOOuusWJ1Dg8dgJTMc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JEkqARN/kiRJkiRJkiRJUgmY+JMkSZIkSZIkSZJKwMSfJEmSJEmSJEmSVAIm/iRJkiRJkiRJkqQSGKarN0CSapn+8gPDUL2HdydJquqTTY9z70iSJEmSpFbvrD+be0OD3DRXvBS6I2f8SZIkSZIkSZIkSSVg4k+SJEmSJEmSJEkqARN/kiRJkiRJkiRJUgmY+JMkSZIkSZIkSZJKwMSfJEmSJEmSJEmSVAIm/iRJkiRJkiRJkqQSMPEnSZIkSZIkSZIklYCJvx7g5ptvDldddVVXb4YkSaW0ySabdPUmSJI02BhfSpLUMxirSmovE3/dwMUXXxxGHXXUivc9/fTTYaeddgrzzTdfu19/0UUXDbvssksYknz00UehV69e4eWXXw7d2cMPPxy388cff2wTiE855ZRh6KGHHqzfW3faFknqKNq+4YcfPow88shh9NFHD4ssskh4/vnn2/16f/zxR3zNscceO/Tp0ydMO+204dxzz635HM6pI444YtwGbrPMMkub9n3ppZcOY445Ztw+fn7zzTdb7z/qqKNan8dtpJFGiq934403Vn0/zt9bbLFFfE22cc455wy//vrrQI/bb7/94mtxjs+dc845YeKJJ47vtfzyy4cvv/yyyb0kSeoOjC9DOOSQQ8Kss87a1V+FJEmDPFat5IQTTggzzzxzjAsnnHDCsMcee4Q///yzZrs5zDDDtIlBr7nmmtb7jz766DD55JPH1xt33HFjQjKNHxIrb7nllmGyySYLo4wySoyVL7zwwprbt8Yaa4Txxhsvvh7PO+KII5qKvW+55ZbWz8fzTzrppA7sLamcelzijxMLg1XbbLPNQPdtv/328b5mqiEqJTs6G69f6Xb11VfXfN73338fNt988zgwN+mkkw70msUBu2oYJDz88MPDoHDZZZfFAcL333+/ze+/+OKLMNpoo4XTTz89lM15550XB29pBEnYzjbbbLEBbI/5558/Dqz27du39Xdbb711bAA//fTT+L1xPK+yyioN/21wG3bYYcM444wTllxyydjY/vvvv4N1W/DVV1+FHXfcMXYM6NBMNNFEYcUVVwwPPPBAQ8+XpI469thjw88//xzPR/PMM09YbbXV2tx/6aWXhummmy7OqieoIOD64YcfKr4WQdBpp50W27cBAwbEtvXAAw8Mjz32WM1tePLJJ+M2cHvllVdaf8/7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TNxf6XbNNdc0sYckSWWNWwbl+9H+zDrrrKEsBud309Nj/UknnTScfPLJNR9D/4liaElSz4ibKznhhBPCzDPPHOPUCSecMOyxxx7hzz//rPmcQw89NIwzzjjxOeuvv374+eefW+/bc889wzTTTBPj2skmmywcffTRbZ57+umnhznnnDN+rlVWWaXu9h144IFhpplmivFwsV2tNw7A2D0x9phjjhn3Hz8Td0vd0VDdvbKAjt8222wz0H3bb799vK+Z6oOHH344PufHH38MgwqvX+l29dVX13ze999/Hwfk6OTSIW5v5/fGG28Mhx9+eBiU30e1W3G7hwSDM3B98sknw3LLLRdGG220MMIII8RG6sQTTwz//PNPGJxorGngjjnmmIr3c/zRWP/111+Ddbsk6dhjj40BwldffRXmmWeesNpqq7XZKZdeemmYbrrp4sx6OvIEOT/88EPFHUcQcNppp4UvvvgiDBgwILavBAiPPfZYzR39yy+/xCIeEne5l156KWy33XbhnHPOia93xhlnhM0226w1SJhkkknie9AfYJsIjpZffvnw22+/VXyf448/Ptxxxx0x8Pj6669D3759wwYbbNB6P9u9+OKLh7XWWismBL/88svYd8qtsMIKcX+l29prr+1BJKnH6umx40gjjRSmmmqquI0vvPBCm8dxfn733XdDd0l01YoJuX300UeDdBt4fd7n5ZdfHqTvU+kYoH0lDlt44YVD//79B8l3U+3Y62isz0Bm+o6IJ6effvpw5plnhsHlueeeC1tttdVgez9J0qCPmythnPKCCy6IsS3xKu0a46fVXHTRRfHxxNqffPJJfB4xdUKbRRtIu3jXXXfFmDpPxo0//vjhgAMOCFtuuWVD2zfllFOG4447Lqy00kpNjwOwHzbddNPw/vvvx/0399xzh2WWWWawj81KPT7xByrZSZrlA1+///57rJKfeOKJu2SbWlpaYqV9rRMWA2z5rV7FwRhjjBHeeOONMPvss7drm1LlBNUGVEAMCqecckqbz1T8rHTk27PNqu+mm26KDS2VMg899FB4++23w8477xyOOOKIsM4668RjsprOTsANN9xwcXCZ776I7WAwYKONNgrDDjtsp76vJDVzntp4443Dp59+Gr799tv4u88//zwm2iiYWHfddcPHH38cgwM69pUMPfTQrVWASANldPBrYRbe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gw4KDz/8cNVl+Omnn2KhD4FGPvnGsqUHy8J1ZYUVVojPs0wnnHBCuO222+Iy8f5VVlkl/PXXX2W/56yzzmr1ebQPZphhhjD33HO3et3zzz8fbr755jDxxBO3+j2Jxy233DKceOKJVddHknqqRownO0Na7vSYcMIJw1prrRXeeeedblumN954I3a2XXbZZa1+//fff8fr29prrx2aTdr+FPzmC4noWOQ59lV3ooCJDlwKmiod6998803YaKON4mvofKUfg3ZG1p133hkWWGCBMOaYY4bxxx8/Hm/ZGK9aEW6+/yMfby+88MLhvvvu69D1liT1nDi7nHpj04MPPji8/vrr4ZVXXon9jfRZb7zxxi3Pk1yjCPeAAw4o+37aiXj//ffDu+++G3799dcYw1dyxBFHhEceeSR+38svvxz7BCjsTSaZZJJw4IEHhm222abqcpM8nGuuuQqto9TwI/4mn3zymDT75ZdfWn7HHxsBwhRTTNEty1QqlVpl7fMuuOCCeFLJPqpl80FDnxNDvjOuqN9//73lxEXjujOccsoprdYpv65PP/10m5a50c0666wt2+Dxxx8P008/fVh55ZXDsGHD2vyZdOIS9DbrNpt00knjRT/roosuir+XpK4w8sgjxwrADz/8sKVyj4KEFExssMEGsZFP45wEXzkUMcw+++wtz6dOqWqj8EBwseGGG8brRTX//e9/43KMOuqo8efrr78+bLHFFnFk4UgjjRQGDx4cqxZrJRqzn8f65a83W2+9daxAZJtkzTfffGGTTTYJ0047baHPl6SeqBHjyc5CBxjFKldffXWMPasVj3Q2ClGOOeaYWBGfYktQ4EJCkuKVZj0eiaGzuL4zSqIn+Pnnn+OoCIqRKiHpx/Fz9913h1tuuSU89NBDYdttt215ng7S1VZbLc5MwGwxJAG/+uqr4TqB65H6HR599NE48oJ4uzsT15Kkzouzy6k3NuUaseqqq8ZrBqPseO+LL77Y8vzSSy8dR/FV6ofk/TzP9Zl+9vXWW6/V+/POP//8uE4U0/Ig5if+TrgGkhtgeSq58cYbY3ENyyr1isQfiTAax9lprvg/QVo+A06lHNl3KgdGGWWUsMgii7Qko6guY0gwGHabre6s9r5sheTtt98e5plnnnjCIItfCZVrE000UasHn1vtD5v15DVM33XooYe2BIJpFN0aa6zRalRdmtbjvPPOC1NPPXXL5+en+mTd9tlnn7gNWe7pppuu1YmHkWmcPHmOE9O+++5bMQilui67Tvl1paqh2mexbFQusHyc6JZbbrn4e0YuEPjRsck+ovovX13I9mYkHa9hXdhfjJjIrue//vWveMKmCoTqkny1JJ/LcUNlKduTUZZ5Z555ZryIcKGaccYZwyWXXBJq4UKVtsEss8wSDjvssFjlQhVrwsWNzmGWjeXfcccdW1VFporHm266KX4G2/CDDz6I+5sRGptuummsqEwBFfuUbca6cMwwwoRh5VmM3hg4cGA8NtjerHO1UaR8P8uRPPXUU/FvjPczHH3o0KGtXk8nAdWdHH/sF7YXyeEiaATkA15+5veS1BXoAOZ6yPmRdgHolOL8SCU5OLcts8wyNQtq6HziXMn5m1EU2fNt3pNPPhnuueeeeI2s5qOPPoodZSTlEgpC6CzO4ucXXnih5vpSmPLmm28ON7LlpJNOCv/4xz9ixaUkNaNGiydrtcHx0ksvxdHgdEZx3aGDiGtYLSwfcdpiiy0WK+GJ31KxSq04iOXnNXwv10dikGuuuabVa4rEKFkk/eaYY46W6vfXXnstLhejzkgecQ3mOk0cynUqP1U1y3T22WfH6zDfyUgCrnesE7EnsRejB7NTe/F/klJsN7Yf8RLX5XIJMDopaQNwrOSn8q53XRPinXwims7CcnFQvd/BuvE6Ym7aB4ykII7keOUz2He0BaohVqeNwmi9cl599dVwxx13xH4IYm6OdWY/YJ1IKuOZZ56JsSKjHzim+BskVicJWGQblZP6HWabbbZ4HLL9SDxKkpo3zm4ProXE04xAZJno76Tgqag999wzFkoxqIP+aUYqVno/11vi9+z0nPyfft2ig0J4Hd/ZrIVP6rm6/R5/NLizSQIaxlS85w0aNChce+21ceQQQQFJLpJLZMsJ9nguVTpSLZaSFNXel0UDmKpEGrt0knUEqvRpjO+2224x8CJw4WR05JFHxudTwJgq3LIBJAENy03gWum+a3w2J6dTTz01Ljefn6oJqbhYccUVY7DDNF80oDk500CvV9HPYhsTTFKpx8mMChCqHjh5sg50cOY7QwlgqDpkehA6N6+88soYKHMST/g/QR4BB69ZZ5114ntSYENHK0kqXsf3ELTnl41KS/bDXnvtFYPp7bbbLh5nzCNdFEE/+4rAhIA56du3b9wHVEayDZiahOMuH1wyNJ4gitcRmOPf//53DIgJ+gn2wMWR44RjhuP43HPPjZ23ya233ho7ntknvO/ee++NSdmiSEoSQNOJTeBGoplgLYsO6MkmmyxeCFkOgnQqQ5knuxaqbrgwpg4P/uXnWhdhti/T6WUfklSP/fbbL56j6QxktAfX0FRpSIEG5z7+pTCG83WRjlSq3SlGoWOXa1UaoZdHZxedm2ecccZwo+vyuJbQ1qCDOFlppZXi77lGcD7kmkDHWpFzIdcW1o2OzmwVIyP9jj/++Jrvl6RG1ijxZJE2OJ1PjKQiOcj9c0jCcD8YqtLrka5VzChSNA7iusN1jniPUV/rr79+XJekVoySRycg+4WYmNeSSOUziRV++OGHmAwjTmBqTEbJE9vw+6xUJEmMx4h4RtSz/Fzv2T4kwLJxI9uYzyE+Ik4iZiQGoXMui5GHKfFK0eYOO+wQ93tb1zXhuk5xZzqW+F5GzJWr7q/nO4iBScKx/lzbU2KabUBxKbEy24J1b2vyDXwO7Si2TXbUBPEuMXdaR35m39JOoTOTRDKvY8aC9soeu+UYM0pSc8TZ7UE/KoVDFDxxPaU9UU/cS5Lyiy++aLlnH32WrGM5aWBHdgrr9P98u6US2pJct2vNCiQ1XeKPOXj5A2UoMA+SRtl5eUGHG8km/oipZCNYomFMo5AEFNNx8YcKEipUi3ECqPW+LEZyUZFA1Vr6rHIYtkxyLfvIBxIJo/sIAAlqqM7j8wleSNCB+fCzFW7p59TQZbpEgr5ygSMjzkjCENiSBOLz//nPf8bhyaDjkQCWwIAgiSHHLA9BTrlpJqsp+lmcwI477riYFOORKkt5HT8TQOZHIxx99NHx91Qf8n6qNkmise5M08O2JaggAcWoQD6PAJnAJwX4BEoEdZxIqZqkIjeNOExIsPHdBHa8hkoLkpL8vhqGeqf9zHHD60m2MkIvYdlJNhLkEaiTdMwnyAjA2I6sH9uCqkzweoJw1isNaWf4OK/j8whUWd/s55E4JmhmH1D5ygWv0gWqHC7S7Df+BpjKlAv03nvv3eo1BG18PkEfo/7YR3QQFEn88V7+hjk2wb/8XCsQ5Fjg7zY9OOYkqR6cR+g0pfCEUeLZ0XJ0UtH5yYPnOJ/ReUsnVy20MxiNQOdrpYCC4g6KMBhpUQ0dc1y/KFjJ4hpFxyMjFSi8oDONdgvThVdDIMK65D+PUeRcj6q1aSSpGTRKPFmkDU68RfzHfWOIu/g/bWmSdNkZR6ohaUnMwrWOuKNoHERxJYWavIaYlTiA0V5JrRilnCmnnDKcfPLJ8T6M2WQqMRD7iHUknmHEHYWS+XupE3+Q9GSZGCHHyEziEmI93kdCMzsTDHERiUFGjhFbsh7sD5JjWSTI2B60A/hcRi5kE6FtWddsIjrFQST2+K5snF/vdzz22GNxhCPPp+JWCmBZJwp/iJFZ7yFDhsSC3fzML/Vg5EQqUE3o2OV45jkQG951112xKJTRrfRlMBIiv+wkBPP9JrWmPOUYYLukdlc5xoyS1NhxNm2CdE0od5/mIrhXMP2yFGFx7eBzuB7y/1poi9FeI/lHLM2D/y+77LJlX5+uXdnRfen/RUY1UgBF25T2htTrEn80gqlyp1FMRxj/z8+Jy6gwEidp2DBIItDBlq1CzKvnfdmqtmqowqPiMPvgJp7lUC1JAJht6DIagKCn1smIIKlcgJDwvdUaxKzfggsuGKsBk3RSo2Fej6KflR25kN7HFCFZfE5+G7Hvs9uIQI4TMVPAkHij85NgL/sagsI0rUuR7+E12eMgrUO14wcEy2k/U5lLpyxBMdWVCdPHkHTlAsdJn4pOphrN7mNGf5RL4JY77hj1yLLR4cC6Evxkk8ssC9/XVqkKOTtFbX574fTTT4/7lOOQ5SAgr5TkLhfwkqwlQOTf/H2nyiF5ycUzPWhQSFJbcD6mY5bGdZqaKmFKKgIRRk9zPs9P71UNbYpK02hxLeB8RxuGB6PUKfTJj8hmFALtgHynNNdY7hXAiH/ul0DhEKP2aiUS+R6CHjqk89+Tpt/mwTmVURN77LFH4fWVpEbQKPFkkTY4sREJqGzcQ3IsLUs1FI1QiU9sSsKSUWfEIEXjoPyy8HP2NbVilEpI3lGRz9SfqXiSQhriYpJzJFj5PbFl/vOy8VMa1c6IguzvKBZNo+P5DBJkJAVJSLGcrEO1z+X6yzpR+d/edQXXdzo7uYZzTFaKg4p8Bz/TOcnsKxSLJqwTCblsDEyhELFrrfi2vYjv2HcUNzNjEXE5xxmdsNkpy4mL8/0mlWYySsXVvIfjluR4pVmYjBklqbHjbGaISwm3tk59yYh9kn2M2OMaxAAQ+qcZRV8LyUIKxXgPgzJ40EZhZHu5kYp8B22s7DWM/zNYgTZMLcTltAlon9E+5buYgYH/Z++DLHWG4nfa7EQ0htMUHSQbugNBUhE0zDmRFcFJjFFT5W50Xe2+gEWWp9JUY92p6DbMbyOqMjnh5nG/BapISHCSdOPfrK64SToXkOz+puqWKkoqVy+99NJYdUq1LglBRuJRDUnFMSMvGLWZRvaxv7KJ00rbjCCRKlaOGxKgXETo1GXUZNF9z/fk7xNV75QvfCdBM99L0E8QRqVzmuKlFgJyOikI4gi8qbqtFOglVIzykKSOQOBBhTyjJhhBQcKOByPEQacoP1NtXw7nLBJwjDCnk5d7CFBNT6BTDkk/pp9KGFFBR2Z+6mk6s2gXZKcKARWUdIRS6EIAwHWFEfaMCqmGz2MkR/4amS+e4FzOtHKpTUKBDdepNJUWHadF2ieS1BM1UjxZKzZi9BejyPNIntWqKOe6w4itjr6vTpEYpRqSVGlKMJA0olCSEYAUvBIDcJ3KT++YnTEkxVLlfpdmoSF+4d5wjGYkhiNuIiFV7XPT56TPaO+6koAjPiQe5NpKYU5+KrCi30FSm45CZpzhGM/OOtMZ8glQ/Pnnn7GTlOfS3xfLy0w/CXExHaDEiun+gYwAKdpvQnE1U4XyudWKn2HMKEmNHWeXU29sSpuBuJwR71zrKbjltem6wwAS+kF50D/K53Gt5xpCwo3XcT0bPHhwfD3/J7mXLxzLFjHR55sKqVh3ZknIXivTg3Xh+7gO0qdMv0D2tfQbMGKf/oX8KHup6Ub8gZMDf9z8QeanaES6ETlDYxNeS4UZ060g3U+HP+563tfZJ0PuFcAJJf/gBJCCjuwyF0VihZNJfjqUJN38PJsAYjsQBHIyq0dbP4v3cQP7LO7hkN9GVGSU20bsOxJtbB8CkPzzKfjge/IJqfz38JrscZDWoS3HAZ2r6YbtJCTZDwRpBDl02OarXurBVC4Ev4z6oGqYKlgqUbKofqRipBKCpWzVCBfc7OhDtgUJ1XQhLbe92DZcpJkCh33A9q5VZZxHcMrUO0VG+0lSZ+BcSqOaJBjXFCoKOcdSTc75letI/t6zCY12prFiNAGdePz/xBNPjPfXyRag0NGazr1cE9ODwg+eT9cq0HHGFCjZhn828cfU3bwnVUtm71nF9+QLXrh+pvvc5mWXhQfXLtYj3YSdew4RJNHuYpQ1/++JRUWS1CzxZJE2OOd/7vXK9I/52KdWYpEpGFnefNKvaByUXxZ+5r1FY5R68P0UfjINJgUudMR1xP2A+FyKYbieEi9zDaZQsx4dsa4pDmKkfb4wp57v4LrMvYbpzOS4TglE9gvtlGwMTCKVvof29HPQkUp7hBg34f71xLtpdCFxZerLSNI61ntLkXxxda2knySp8ePscmrFpiTasjPcECeTYOS2VyTruF0UgzRScS33nuX93P6Cthf/Z1R8cuONN8b7NjOCkcIq+q6z04IzmjA7DSn3QeYayfWXBwlA+gcSin35DpKDN998c/x/mjqUop1sXE48Ti4gxehS04/440BPU1KUO+gJcqh85x4IjKhiJBgVZjQ6U2cXJxiy9zSMCSD4I6ODrNb76kVDOM1vnxBclQvEmJKDaj++l0pDGshM38KQ3jQCgKCOJA4nDQKe1CFXC++jUpKggnviUeVAsECCjPsgkLBhVBpDiKl+JQigkoFKg3xDvZa2fhYnSRJibH86OQkgmO4ki+HhJMz4XF7DdqQjk0pNKkdIpFENSdDEZ5GEYgQG24wEGFP5EDSy/ajs5N5IVE3ccccdrb6HZWC78H6qCTkRczNapmarhoAq7W8CLaZkYfnS3MwEKAT/3P+C6lyCzbYOVQcXSKZ0oeJz4MCBcYg8ncRZbHum+iSw515/LONtt93WskzcM4Ntx0WJjgt+n61qpdOaizRTtDBVCsFw/h4fLAcXTrYlnQhcNOng4P9F8fkM78+PapGkzpC9x0/CeTDbwZoa83QK5q9HeXTEcd6rJt3ou5xyn09bJLs8+et6talJuGdB/vvo3CvayZbv+KRKMz86XJIaVSPEk0Xa4DvttFOsYGfWDO5fzncyBTSxAR1sbekgKhoHUYHOtY+R7oxwpxMs3cewSIxSDz6P+ILvY5pOlrEjik/4XNaNuIx9SUddvcmojlhXEtHErJVG6NXzHRy7PE+HJw/iXN5P3MuxxCgH+iPoYKUDk99XQlzLg2MK3FaD93Jcc6zRmcmy87nEtMS5xOnEnOn2JsTfjNDjliYcp8TIdH7y98MxJklqLh0dZ5dTKzbNJtlA0uyaa66p+HqWg0clxNH0d1aS79elT5VRgZVmlWBmHR5F1Fo2qelG/IFGcbWpK4455piw1lprxfunUQlJY5U/0pQoo5HLVBk0eKnOT1O91HpfvdI9CrKP7E3Ps6hUIHDk5tc06Elw0UimUZyQzCLJxdQY9TaUudE8CUUSc0yrSAOdioe0PUgGEbCRFCQJR3DKvQPq1dbPIoCg2oOqC97HiZMqjSySd4xa5Gb1dGqyDUiYZu+bSCUHiT/ua0CFBlOf0RnL54PtSoDMVDF8D9s7v2y8h+cJrqkqJUDic7m4VEPFbdrPc845Z7xJLdud5QHfxwgQpuNhOkuCZG5621arrrpqvP8Sxy/fRzUoAWsWy0xgzoWV15Doy46s5JjieGJ70sHAlDdpylHQgUHAT6DH9qYDIj+dENOvMh3ceuutF6s7qSDlOKsH0/lQeZOd1keSJEnqjfFkkTY4MRCFhBTvUSnOqDXu10ohXb3Fm/XGQaw7iSjiMwoAmV4yjR4rEqPUg4Tit99+G7cn25VCzo6Y7oq4jP3CzCUk/4jH+Y56dMS6knQkDkqjSNv7HRw7t99+e+wUJfFGzM8+5H7sFBrTActzxOz5aUyziMc59ug3APcR5ufsKAfiWfoWKDQlAU4iOHufJmLPyy67LMb4vJdEIQXMJCSdOUCSJKnn6FOy3FtdXCmy5JJLxkDPkWCqhupf7vMw6em7hr6jeu8/Sf/PB1v8v/vKSJKk9iFRxYgzkoRSI8aMTA3X2fdAlCSpM72+kSPnG9WMQ4aGnqjHjPiTJEmSJEmSJEmS1HYm/iRJkiRJkiRJkqQm4M231KVq3bBVkiRJktR1jM8kSZKk5uKIP0mSJEmSJEmSJKkJmPiTJEmSJEmSJEmSmoCJP0mSJEmSJEmSJKkJmPiTJEmSJEmSJEmSmoCJP0mSJEmSJEmSJKkJ9CmVSqXuXghJyvv+++/DgAEDwrBhw0L//v3dQJIkSZIkY0ZJkqQaHPEnSZIkSZIkSZIkNQETf5IkSZIkSZIkSVITMPEnSZIkSZIkSZIkNQETf5IkSZIkSZIkSVITMPEnSZIkSZIkSZIkNQETf5IkSZIkSZIkSVITMPEnSZIkSZIkSZIkNQETf5IkSZIkSZIkSVITMPEnSZIkSZIkSZIkNQETf5IkSZIkSZIkSVITMPEnSZIkSZIkSZIkNQETf5IkSZIkSZIkSVITMPEnSZIkSZIkSZIkNQETf5IkSZIkSZIkSVITMPEnSZIkSZIkSZIkNQETf5IkSZIkSZIkSVITMPEnSZIkSZIkSZIkNQETf5IkSZIkSZIkSVITGLG7F0CSqpnl0oNC31H7uZGkBvHBFsd19yJIkiRJkiT1Gq9vNFd3L0KvNeOQoaEncsSfJEmSJEmSJEmS1ARM/EmSJEmSJEmSJElNwMSfJEmSJEmSJEmS1ARM/EmSJEmSJEmSJElNwMSfJEmSJEmSJEmS1ARM/EmSJEmSJEmSJElNwMSfJEnqMTbffPPuXgRJkiRJktSF7AuQOpaJvw7y3nvvhT59+oTnnnuuoz5SGYccckiYc8453SYFcBzecMMNnb6tLrzwwjDWWGO5TyTVtMQSS4R+/fqFMcYYI4wzzjhh8cUXD//73//avOV+++23+JkTTDBB6N+/f5hpppnCOeecU/H1v//+e1h77bXDVFNNVfYcma7hLF96rLLKKq1e8+ijj4Y55pgjjDbaaPF69Pjjj1ddxpNPPjlMM8008bOWWmqp8NZbb7V6/sgjjwxTTjllXP655por3HXXXS3Pbb/99q2Whe9k+Z599tk6t5QkSepMtC245kuSpM7vCyjn/vvvD0suuWQYMGBAoX5K+phHHHHEVjH3lVdeWfj5o48+Osb6xPITTTRRTFh+9913Fb/vP//5T5h33nnjdlh99dWHe/77778PG264Yfy8CSecMBx++OGtnn/mmWfCIossEp/ney+++OI6to56sx6R+OMPhA4tOrrydtppp/hcPVn/Bx54IL6n2h9dT5SWOz34Y19rrbXCO++802OTSeyXcietnmaXXXYJM888c9nnPvjggzDCCCOEm266qccnf/OBZalUCv/617/iyZ/jB59++mlYYYUVOvV7sd5664U33nijQ79HUvM69thjw48//hg+++yzMP/884c111yz1fM0XjlPX3755TGhR0Dw7bfflv0sGuGnnXZa+OSTT2Ij+brrrgsHHXRQePjhhyt+Pw3lSy65JEw22WQVX/PRRx/FZeRx8803t/z+m2++CSuvvHLYeeed4zLRNuHnSu0M1uGEE04It912W3z9QgstFBOJf/31V3ye6+m///3vcMstt4Rhw4aFPffcM6yxxhrxe3DWWWe1LAcPGv4zzDBDmHvuuWtsZUmSOk82Vi33oKNMHY8CJzoLaUOV61DdfffdW35+9913Y+fhJJNMEkYZZZTY7llttdXCa6+9VrM/Jj3GHXfcsPzyy4cXXnihKQtYJUmN2xdQzuijjx623HLLcOKJJxZ+D/F8Nuamj7Po8xQV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cx/3rv088sgjh57GxJ+kHqlv3/+7BSlJP6vsi2Nbub3cVp3BY8tt1Vk8ttxWHluSpLbGjJNNNlmv23i2nXoH93Pv4H5ufu7j3qFPDyxA+r+edUmSJEmSJEmSJEkNzcSfJEmSJEmSJEmS1ARM/Enqkfr16xcGDx4c/5Xby2PLv8VG4HnL7eWx1TP4tyhJakZe33oH93Pv4H5ufu7j3qFfD+6/7lMqlUrdvRCSJEmSJEmSJEmS2scRf5IkSZIkSZIkSVITMPEnSZIkSZIkSZIkNQETf5I61YUXXhgeeOABt7LbymOrm/m36Lby2Op+/h26vSRJvZftgObnPu4d3M/Nz33cu1zYpH3XJv4k1WXzzTcPffr0iY+RRhopTD311GHQoEHh119/bfeW5JajBx98cJh44onDqKOOGpZeeunw5ptv1nzf6aefHqaaaqowyiijhPnnnz889dRTrZ7nOZb3iiuuGO69s846a3yOk3wjbavrrrsuLLvssmHccceNn//cc88Vet/VV18dZppppritZp999nDbbbe1en6JJZaIn3fMMccM996VVlopPnfIIYeEztBZ2+uPP/4I++yzT1zf0UcfPUwyySRh0003DZ988knDHludfXyxjzlO2F5jjz12/Ft88sknG3Z7dea2ytp+++3jd5x88skNu606e3tlPzs9ll9++YbdXp19bL366qth1VVXDQMGDIh/jwMHDgwffPBB1ff0xvM88sdVehx//PENeWxJknq+rmpjJp999lnYZJNNwkQTTRTbBXPPPXe49tpra77Pa13j7GM8/vjjYamllor7uH///mGxxRYLv/zyS9X3uI8bbz+nPrAVVlghfu8NN9zQ7v6ytA5PPPFEq9//9ttvLX1HzZjc6Gn7+Jtvvgm77LJLmHHGGeO+mmKKKcKuu+4ahg0bVvV97uOOY9/1/68kSXXYbLPNSssvv3zp008/LX3wwQel66+/vtS/f//SoEGDWr3uvvvuKy200ELxubHGGqs011xzlc4444yqn33MMceUBgwYULrhhhtKzz//fGnVVVctTT311KVffvml4nuuuOKK0sgjj1w6//zzSy+//HJpm222id/3+eeft7xmyimnLE0++eSlZZddttV7H3/88dI444xTGn300UsXXHBBQ22riy++uHTooYeWzj333BKn8qFDh9ZcnkcffbQ0wggjlI477rjSK6+8UjrwwANLI400UunFF19sec3iiy8et9WMM87Y6r0fffRRqV+/fqWJJ564NHjw4FJn6Kzt9d1335WWXnrp0pVXXll67bXX4n6fb775SvPMM0/V5enJx1ZnH19Dhgwp3X333aW333679NJLL5W22mqr+P4vvviiIbdXZ26r5LrrrivNMcccpUkmmaR00kknVX1tT95Wnb29sp+dHt98803Dbq/O3FZvvfVWXPa999679Oyzz8afb7zxxlbrnddbz/PIHlM8OF769OkTz2ONeGxJknq+rmhjZi2zzDKlgQMHlp588sl4fTv88MNLffv2je2ESrzWNdY+fuyxx+JnHH300TEOI34ljv31118rvsd93Hj7OTnxxBNLK6ywQuzT4Tvb21/G59Bu3XbbbVu99/LLLy9NMcUU8fn777+/1Bt15T4m9lpzzTVLN910U4zh7r333tL0009fWmuttaq+z33ccey7/j8m/iTVffJcbbXVWv2OCxoXw+Tbb78tjTnmmLED7bDDDovJqauuuqrqxfLvv/8uTTTRRKXjjz++VcKGTkgaKZWQwNlpp51afv7rr79ixzsN5Wyn3b777hs/iwt8wvLtsssusfHUWR3CnbGtst59993Cib911123tNJKK7X63fzzz1/abrvtWnUI77DDDqVxxx239Mgjj7T8/sgjjyytssoqMbHRmR3Cnb29kqeeeiput/fff78hj62u3l7Dhg2L2+uee+5pyO3V2duKhMmkk04ag3PWsVbirydvq87eXuU+u5aevL06c1utt956pY033riu5fE8//+wX5ZaaqmGPbYkST1fV7bHQbEJBaBZFKHwmZV4rWusfUx8TuFWPdzHjbefQR8OMSSJqFqJv6L9ZXwOxw9Jq59//rlV0cBBBx3U6xN/Xb2Ps/gcCg7/+OMP93EXsO/6/zjVp6R2eemll8Jjjz0WRh555JbfvfXWW+GHH34IgwcPDpNPPnmYbrrpwjrrrBN22GGHip/z7rvvxqlLmK4gYWozpt1iqotyfv/99/DMM8+0ek/fvn3jz/n3TDjhhGG55ZYLF110Ufz5559/DldeeWXYcsstQ6Ntq7Zim2S3Fdgm+W3F8m200UbhggsuaPkd05h15bbq7O3FFAtM8TDWWGM1xbHVmduLbXHOOefEv8c55pijKbZXR26rv//+O065tPfee8dp/2pptG3VGccW08tMMMEEceoTXv/11183zfbqqG3FcXXrrbeGGWaYIa4T24vrYa0pgDzP/5/PP/88br+tttqqaY4tSVLP19nx3kILLRSvP0wjR1uBaaiZpo5pvMvxWtdY+/iLL76It1eg3ce+pv2x+OKLh0ceeaTie9zHjfm3TFtyww03jFO0MnVvLfX0l80zzzxxqvo0DTC3CXjooYdizKqu28fl+qCYunfEEUd0H3eDl3pp37WJP0l1u+WWW8IYY4zRcv8gGqh0eid05o433nhh3333LXSPPnDiTCe5LH5Oz+V99dVX4a+//ir8Hk6UJLAohLrmmmvCtNNOG+acc87QaNuqrdgm9Wyrq666Kvz000+xkUgjZeWVVw6drSu2F8Ex9/zbYIMNYsOrUY+tzt5e2c8+6aSTwt133x0/q1G3V2dtq2OPPTY23pmzv4hG2Fadub24n9/FF18c7r333rjtHnzwwXhfC7ZJo26vzthWfMaPP/4Y78PHNrvrrrvCGmusEdZcc824zSrxPP9/CJTGHHPMuL0qaYRjS5LU83VlvEd8xv3LuVdXv379wnbbbReuv/762FlZjte6xtrH77zzTvyXey1vs8024Y477oj3cfznP/9Z8XPdx435t7zHHnvE5O5qq63WKf1ltFvPP//8+H/aryuuuGIYf/zxQ2/XXf1z/J0efvjhYdttt634Gvdxx7vFvmsTf5Lqt+SSS4bnnnsuVqNtttlmYYsttghrrbVWy/N0tt13332xMoEKplVWWSWsuuqqYejQod26uVdaaaXYkUoii0ZQV1TqN+q2YmTX9NNPHzs32VZUh1WqTGqk7UWgvO6668aO2zPPPLOhj63O3l7ps6mKIvHAdqNh3BGa5W+Rqq1TTjklBlOMIO0MzXZsrb/++vF1BFqrr756bIw//fTTHXaT+WY5tqjiB50BdAyQYCIApQDjrLPO6pDlbtbzPFgfRq4T1Df636IkqWfrjOvaUUcdFTun04MROzjooIPCd999F+65557wv//9L+y5556xjf7iiy92yLp4revefZzafyR0+Y655porFmCSjEhJHPdx4+/nm266KX7OySef3GnrsvHGG8eRRCSTu2P2pp6qK8/Xyffffx/PrbPMMktM6ncU93Hz9seu1IFxZ+dH95Kazuijj95SVchJiM7D//73v62m1KJTl6kF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26mnnho23XTTMNJII4X1118/9ITtO9ZYY7X7s/7xj3+El19+OXz66acxWTj66KOHzsA2O+igg8LFF18ctthii075DkmSJEk9n/Fi12xf40VJRZn4kySpF/nll1/CqKOOWvf7xh9//PhIXnvttfgvo+bGG2+80JOcffbZYfrpp4/Llpdd3iWXXDJMPvnk4YILLmiV+Pvss8/CbrvtFu65557wzTffxFGGM8wwQzj88MNjwNUZ8tu3vcYZZ5z46EwjjDBC2HzzzWMC1cSfJEmS1PiMF40XO4rxotS9nOpTkqQGmdqF6j6ey2Lk3cILLxxGG220OKUjU1MOHTo0PvfAAw/EqR55zdprrx369+/fMv3l+++/H3/H6DdGhC233HLhxRdfbNdy1/pMRp/xGkbjpWkombIEjBpbZJFFYrIqrcdTTz3VpuXgs1iOWlhGEoQffPBBq99vs8024f777w+nnXZaTBReffXVYbXVVgtffvll1c9L2/vOO+8M6667btyHU0wxRbjsssvi8yTI+Jl13HrrrcNvv/1WceqWath+U045ZdzOq6+++nDLVXTf8p2MDhxllFHCpJNOGg444IBW03Z+9913cVvwHK8hSZofGcnx9Nxzz4Xnn3++5nJLkiRJaj/jRePFaowXJcERf5IkNagrr7wybLDBBjEpRXJp5JFHDo8++mj4+OOPw1xzzdXyum233TZsvPHG4frrr49Vdz/88ENMrPXt2zecddZZMalz5JFHhsUWWyzeH44ET72KfCbfzxSfJPj22muv+L5pp5225Z52TLvJz7///nu4/PLLW97LaLui3nrrrfhZJENr+fvvv8NHH30U5phjjla/f/DBB8Puu+8eNtxww3DOOeeEFVZYIT6K2mGHHeJIOJJm5557bthkk01iYuyll16K2+add94Je+65Z5hmmmnC/vvvH+px0003hTfffDMGcyQJ99hjj7DLLruEK664Ij5fdN+eeOKJYdCgQfH9J5xwQnj11VdbEn/HHHNMfA3LePvtt8efSdoydSg/Z3GPPxK1d99993DbUZIkSVL3MV4cnvGi8aLUa5QkSVKXGjx4cGn00Uev+/kBAwbE5/D333+XJptsstJyyy1X8XPuv//+Epf67bffvtXvTznllFKfPn1Kr7zySsvvvv766/ide+65Z6F1uOCCC+Jnf/nll3V95pRTTlnaaaedqn72X3/9Vfrjjz9KM844Y2m//fYrvN1w2WWXtVqu/PJ+9tln8bM//fTT0u67717q169f6aGHHmr12hlmmKG07LLLln799dfS4osvXioqbe9Bgwa1/O67774rjTDCCKXJJ5+89Pvvv7f8fq211irNOeecwy1fWu533303/nz11Ve32nbsc5Yru01GGmmkuM2K7ofvv/++NMYYY7TatjjzzDNLo446aumrr76KP88666yFjge20dprr114O0mSJEmqzHjReNF4UVJ7OdWnJEkN6PXXX4+j1bbccsuar83fl+7hhx8Os802WxytlTD95DLLLBMeeeSRNi1Pez+TEWdrrLFGmHDCCeOoxJFGGimu4xtvvFHXcjAqjdFu4447btnnJ5poovjZE088cTj55JPjY9FFF231GqbkZJrRSSaZJI7SY8Tcyy+/XHgZWOeE6TYnmGCCOOKO700Yxfjhhx+Gei2++OKhX79+LT/PMsss4Y8//ghffPFF4f3w2GOPhR9//DFO0/nnn3+2PJZeeul4Tw/WGXPPPXecDvTf//53y+/K4Z6JbHdJkiRJPYPxYnnGi8aLUm9h4k+SpAb09ddfx39JTtVCMi3r22+/He536XXffPNNm5anPZ/J9JTLLrtsvDcdU1CSvHr66afj1JG//vprXcvB60mwcb+8cu65556Y1Lv22mvDrLPOGnbbbbc4BWYW98RjOk7u8UeSbciQIfFeeEcffXShZeBejFlMwVrud/WuW6XPRvqsIvsh3UeQxB7bKj243yFSQpL1Z5pSpgKdffbZ4/0JzzzzzOE+m21EwlCSJElSz2C8WJ7xovGi1FuY+JMkqYfhvmyM4sriZ0ZpJWlE2yeffFLz8/JJMEaApRFiWZ9//nl8ri3a85mPP/54HL14wQUXhI022ijeA3DeeecNw4YNa9Ny/PbbbxWTaiQTBw4cGNZcc814v7oRRxwx7LPPPsO9jvvWcY8/kmGvvPJKvN8d98Bra2K0qxTZD+nf6667LiZY8490P0NGKzIikqpYkqMkZ3fccceYmM367rvvKo6wlCRJktSxjBeNF9vKeFHqPUz8SZLUw0w22WTh999/D2+//XbL7+67777w119/tfw844wzxteRLKsXibUXX3wxTv+SMFKM0XA81xZFP7PcSLc0WiyNXkvTUb733nt1LwfbBe+++27N104++eRhjz32CHfccUcYOnRoy+9LJW6v19rCCy8cf8869WRF9sOCCy4YRhtttJhsJcGaf5RL4jHi76STTmqZljWL/ZS2uyRJkqTOZbxovNhWxotS7zFidy+AJEm9EUm8a665ZrjfzzfffHHE1eijjx622WabOBqNBM0pp5wSKzuzo/i499oGG2wQ1lprrbDpppvGKRcZPceItpVXXrnid2+xxRYxicO9/4444oj4udzHjtFvu+++e5vWp+hncu85kph33313HFU39dRThwUWWCCMMcYYYaeddgr77rtv+Pjjj8PgwYPDpJNOWvdysP34zmeeeabVfe4qYSQfU1oee+yx4Yorroi/m2uuuWJCkH8ZPciyHnjggfG+fCxvT1ZkPzBd6GGHHRYGDRoUj60lllgi3leR6U1vvPHGOA0qiUGSndx3kXsG8vzFF18ck7PZeyL+9NNP4bXXXov7S5IkSVLHMF40XuwMxotS7+GIP0mSugGj3tZZZ53hHg899FAccUXyhSkbV1999XDeeefFpAuJvaz11lsvJmpIlK2//voxCfjII4/ECtBqxhxzzPDAAw/EaS+33XbbOL0mSTi+m1FwbVH0M4866qi4fCQrSVDefPPN8f5zV199dVzf1VZbLU4vefbZZ4fpppuu7uUgYUrilGk8i051sssuu8QkbBphybY844wzwuKLLx6eeOKJOOXntNNOG2655ZbQt2/PbjoV3Q977bVXHC16//33x33BsXfOOefEfZJGXpL447jjubXXXjuOomR/ZROqd955Zxh11FFbpgeVJEmS1H7Gi8aLncF4Ueo9+pTKzWclSZLUoEhOkazjvnaMXGsPRsORSFN5JAUJHs8//3w3kSRJkqQez3ix6xgvSt2nZ5etS5Ik1YlpTpmWk5GS6jyMALz11lvDAQcc4GaWJEmS1BCMF7uG8aLUvUz8SZKkpsL9D88666x2j/bD5ptv3iHL1IyYYpbpQZkGVZIkSZIagfFi1zBelLqXU31KkiRJkiRJkiRJTcARf5IkSZIkSZIkSVITMPEnSZIkSZIkSZIkNQETf5IkSZIkSZIkSVITMPEnSZIkSZIkSZIkNQETf5IkSZIkSZIkSVITMPEnSZIkSZIkSZIkNQETf5IkSZIkSZIkSVITMPEnSZIkSZIkSZIkhcb3/wFXr6u6c+ZwhgAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 1800x600 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "lucro_por_produto = df_analitico.groupby(\"name\")[\"lucro_total\"].sum()\n",
    "\n",
    "top10_lucro = lucro_por_produto.sort_values(ascending=False).head(10).sort_values()\n",
    "top10_prej  = lucro_por_produto.sort_values().head(10).sort_values(ascending=False)\n",
    "\n",
    "fig, axes = plt.subplots(1, 2, figsize=(18, 6))\n",
    "\n",
    "bars = axes[0].barh(\n",
    "    top10_lucro.index.str[:35],\n",
    "    top10_lucro.values / 1e6,\n",
    "    color=COR_LUCRO, edgecolor=\"none\", height=0.6\n",
    ")\n",
    "axes[0].set_title(\"Top 10 Produtos — Maior Lucro\")\n",
    "axes[0].set_xlabel(\"Lucro Total (R$ milhões)\")\n",
    "axes[0].xaxis.set_major_formatter(mt.FuncFormatter(fmt_milhoes))\n",
    "for bar, val in zip(bars, top10_lucro.values):\n",
    "    axes[0].text(val / 1e6 + 0.05, bar.get_y() + bar.get_height() / 2,\n",
    "                 fmt_brl(val), va=\"center\", fontsize=9)\n",
    "\n",
    "bars2 = axes[1].barh(\n",
    "    top10_prej.index.str[:35],\n",
    "    top10_prej.values / 1e6,\n",
    "    color=COR_PREJ, edgecolor=\"none\", height=0.6\n",
    ")\n",
    "axes[1].set_title(\"Top 10 Produtos — Maior Prejuízo\")\n",
    "axes[1].set_xlabel(\"Lucro Total (R$ milhões)\")\n",
    "axes[1].xaxis.set_major_formatter(mt.FuncFormatter(fmt_milhoes))\n",
    "for bar, val in zip(bars2, top10_prej.values):\n",
    "    axes[1].text(val / 1e6 - 0.05, bar.get_y() + bar.get_height() / 2,\n",
    "                 fmt_brl(val), va=\"center\", ha=\"right\", fontsize=9)\n",
    "\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "afa8ecdf-fbca-4f3c-9974-53e61ca57803",
   "metadata": {},
   "source": [
    "## Análise 2 — Comparativo 2023 vs 2024\n",
    "\n",
    "Em 2024 a receita cresceu, mas o lucro virou prejuízo.\n",
    "A alta do câmbio (R$ 4,99 → R$ 5,39) elevou o custo de importação\n",
    "e comprometeu a margem operacional."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "142b6980-7fcf-43d9-ba12-599d7445d470",
   "metadata": {
    "jupyter": {
     "source_hidden": true
    }
   },
   "outputs": [
    {
     "data": {
      "image/png": "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gw8+KKABVEqmBgAAAAAAUBJkagAAAAAAACVBUAMAAAAAACgJDTKoUVZWlqZMmZJ/AgBoSwAAdUm/BAAsvgYZ1Pjmm29S27Zt808AAG0JAKAu6ZcAgMXXIIMaAAAAAABA6RHUAAAAAAAASoKgBgAAAAAAUBIENQAAAABY4px11lmpUaNGFZYNNtigyv1nzZqVzj777LTuuuumli1bpm7duqXHH3+8wj533nln6tixY1phhRXSwIEDK2z76KOPUufOndOUKVNq7ZwA+P6a1sBzAABANmLEiLTWWmulnXfe2RUBAL63jTfeOP3lL38p3m/atOqurNNPPz397ne/SzfeeGMOfjzxxBPpxz/+cXr++efT5ptvnr744ot0xBFH5PbKOuusk/bcc8/0wx/+MO2111758cccc0y64IILUps2bfzmAJZgMjUAqFXxhWH06NGuMpSovn37FkdGNmvWLK299trp5JNPTtOnT//ezz3vyMvCcvHFFxf3eeWVV9Kuu+6all9++bTSSiulI488Mk2dOrXar3HUUUfl5xw2bFilr/3CCy9UWD9jxoz8OrHNexcA1L8IYrRv3764rLzyylXue8cdd6RTTz017bHHHjlocfTRR+fbl156ad7+wQcfpLZt26YDDzwwbb311qlnz57p7bffztvuuuuu3NbZb7/96uzcAFg8ghoALDEdnA888EDq3bt3sUPxtddeW6TH33333flx++67b4X1ZWVl6cwzz0yrrbZaatWqVerVq1d69913K+xTvkM1vjh16tQpp6NHByc0dLvttluaOHFi7gi4/PLL0/XXX58GDx5cYZ+//vWvafvtt0/HH398HhG5xRZbpGuvvXaBzxvPWX655ZZb8v/B/fffP2//5JNP8v/X9dZbL7344ou5fMSbb76Z34eq48EHH8xBiw4dOlS6PUpP3HrrrfM9Ztlll63W8wMAtS/a7fFZHkGKQw45JI0fP77KfaPtHmWnyov2/3PPPZdvr7/++unbb79Nr776avryyy/T3//+97Tpppumr776Kp1xxhnp6quvrvXzAeD7E9QAYInp4Jw2bVraYYcd0oUXXrjIxxT1b3/961+nHXfccb5tF110UbryyivTddddlztGW7dunfr06TNfICY6N+O8Pvzww3TNNdfkkV7nnnvuIh8LLG1atGiRR0ZGECCChhFoePLJJ4vb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66yTDjnkkDR+/HjXDwDqiEwNAAAAgGrq3r17GjFiROrSpUuaOHFiGjJkSNpxxx3TG2+8kZZbbrlKHzNjxoy8FEyZMsX1BoDFJKgBAAAAUE2777578famm26agxxrrrlmuvfee9Phhx9e6WOGDh2agx8AwPen/BQAAADAYlp++eVT586d03vvvVflPoMGDUqTJ08uLhMmTHC9AWAxCWoAAAAALKapU6em999/P6222mpV7tOiRYvUpk2bCgsAsHgENQAAAACq6de//nV6+umn00cffZSef/759OMf/zg1adIkHXzwwa4hANQBc2oAAAAAVNN//vOfHMD473//m1ZZZZW0ww47pBdeeCHfBgBqn6AGAAAAQDXdfffdrhUA1CPlpwAAAAAAgJIgqAEAAAAAAJQEQQ0AAAAAAKAkCGoAAAAAAAAlod6DGs8880zae++9U4cOHVKjRo3SQw89tMD9H3jggbTrrrumVVZZJbVp0yb16NEjPfHEE3V2vAAAAAAAQAMNakybNi1169YtDR8+vNpBkAhqPPbYY2ns2LGpZ8+eOSjy6quv1vqxAgAAAAAA9adpqme77757Xqpr2LBhFe6ff/756eGHH05/+MMf0uabb14LRwgAAAAAACwJ6j2o8X3NnTs3ffPNN2nFFVescp8ZM2bkpWDKlCl1dHQAAAAAAMBSU37q+7rkkkvS1KlT009+8pMq9xk6dGhq27ZtcenYsWOdHiMAAAAAANDAgxojR45MQ4YMSffee29q165dlfsNGjQoTZ48ubhMmDChTo8TAAAAAABowOWn7r777nTEEUek++67L/Xq1WuB+7Zo0SIvAAAAAABA6SrJTI277ror9evXL//cc8896/twAAAAAACAhhDUiPkwXnvttbyEDz/8MN8eP358sXTUoYceWqHkVNy/9NJLU/fu3dOkSZPyEmWlAADCxx9/nH72s5+llVZaKbVq1Sptsskm6eWXXy5enLKysnTmmWem1VZbLW+PrM93333XxQMAAIAlXL0HNaKDYfPNN89LGDhwYL4dHQ1h4sSJxQBHuOGGG9Ls2bPTsccemzsiCsvxxx9fb+cAACw5vvrqq7T99tunZs2apT/96U/prbfeyoMhVlhhheI+F110UbryyivTddddl1588cXUunXr1KdPnzR9+vR6PXYAAABgCZ9TY+edd86jJasyYsSICvdHjx5dB0cFAJSqCy+8MHXs2DHdeuutxXVrr7128Xa0O4YNG5ZOP/30tM8+++R1t99+e1p11VXTQw89lA466KB6OW4AAACgBDI1AABq0iOPPJK22mqrdMABB6R27drlDNAbb7yxuD1KXUbpyig5VdC2bdtc1nLMmDGVPueMGTPSlClTKiwAAABA3RPUAACWKh988EG69tpr0/rrr5+eeOKJdPTRR6df/epX6bbbbsvbI6ARIjOjvLhf2DavoUOH5sBHYYlMEAAAAKDuCWoAAEuVuXPnpi222CKdf/75OUvjyCOPTP3798/zZyyuQYMGpcmTJxeXCRMm1OgxAwAAANUjqAEALFVWW221tNFGG1VYt+GGG6bx48fn2+3bt88/P/300wr7xP3Ctnm1aNEitWnTpsICAAAA1D1BDQBgqbL99tuncePGVVj3r3/9K6255prFScMjeDFq1Kji9pgj48UXX0w9evSo8+MFAAAAqq/pIuwLALDEO/HEE9N2222Xy0/95Cc/SS+99FK64YYb8hIaNWqUTjjhhHTuuefmeTciyHHGGWekDh06pH333be+Dx8AAABYAEENAGCpsvXWW6cHH3wwz4Nx9tln56DFsGHD0iGHHFLc5+STT07Tpk3L8218/fXXaYcddkiPP/54atmyZb0eOwAAALBgghoAwFJnr732yktVIlsjAh6xAAAAAKXDnBoAAAAAAEBJENQAAAAAAABKgqAGAAAAAABQEgQ1AAAAAACAkiCoAQAAAAAAlARBDQAAAAAAoCQIagAAAAAAACVBUAMAAAAAACgJghoAAAAAAEBJENQAAAAAAABKgqAGAAAAAABQEgQ1AAAAAACAkiCoAQAAAAAAlARBDQAAAAAAoCQIagAAAAAAACVBUAMAAABgMV1wwQWpUaNG6YQTTnANAaAOCGoAAAAALIa///3v6frrr0+bbrqp6wcAdURQAwAAAGARTZ06NR1yyCHpxhtvTCussILrBwB1RFADAAAAYBEde+yxac8990y9evVy7QCgDjWtyxcDAAAAKHV33313euWVV3L5qeqYMWNGXgqmTJlSi0cHAEs3mRoAAAAA1TRhwoR0/PHHpzvvvDO1bNmyWo8ZOnRoatu2bXHp2LGj6w0Ai0lQAwAAAKCaxo4dmz777LO0xRZbpKZNm+bl6aefTldeeWW+PWfOnPkeM2jQoDR58uTiEoERAGDxKD8FAAAAUE277LJL+uc//1lhXb9+/dIGG2yQfvvb36YmTZrM95gWLVrkBQD4/gQ1AAAAAKppueWWS127dq2wrnXr1mmllVaabz0AUPOUnwIAAAAAAEqCTA0AAACA72H06NGuHwDUEZkaAAAAAABASRDUAAAAAAAASoKgBgAAAAAAUBIENQAAAAAAgJIgqAEAAAAAAJQEQQ0AAAAAAKAkCGoAAAAAAAAlQVADAAAAAAAoCYIaAAAAAABASRDUAAAAAAAASoKgBgAAAAAAUBIENQAAAAAAgJJQ70GNZ555Ju29996pQ4cOqVGjRumhhx5a6GNGjx6dtthii9SiRYu03nrrpREjRtTJsQIAAAAAAA04qDFt2rTUrVu3NHz48Grt/+GHH6Y999wz9ezZM7322mvphBNOSEcccUR64oknav1YAQAAAACA+tM01bPdd989L9V13XXXpbXXXjtdeuml+f6GG26YnnvuuXT55ZenPn361OKRAgAAAAAADTpTY1GNGTMm9erVq8K6CGbEegAAAAAAYOlV75kai2rSpElp1VVXrbAu7k+ZMiV99913qVWrVvM9ZsaMGXkpiH0BAAAAAIDSUnKZGotj6NChqW3btsWlY8eO9X1IAAAAAADA0h7UaN++ffr0008rrIv7bdq0qTRLIwwaNChNnjy5uEyYMKGOjhYAAAAAAGiw5ad69OiRHnvssQrrnnzyyby+Ki1atMgLAAAAAABQuuo9U2Pq1Knptddey0v48MMP8+3x48cXsywOPfTQ4v5HHXVU+uCDD9LJJ5+c3nnnnXTNNdeke++9N5144on1dg4AAAAAAEADCGq8/PLLafPNN89LGDhwYL595pln5vsTJ04sBjjC2muvnR599NGcndGtW7d06aWXpptuuin16dOn3s4BAAAAAABoAOWndt5551RWVlbl9hEjRlT6mFdffbWWjwwAAAAAAFiS1HumBgAAAAAAQHUIagAAAAAAACVBUAMAAAAAACgJghoAAAAAAEBJENQAAAAAAABKgqAGAAAAAABQEgQ1AAAAAACAkiCoAQAAAAAAlARBDQAAAAAAoCQIagAAAAAAACVBUAMAWGpdcMEFqVGjRumEE04orps+fXo69thj00orrZSWXXbZtP/++6dPP/20Xo8TAAAAqB5BDQBgqfT3v/89XX/99WnTTTetsP7EE09Mf/jDH9J9992Xnn766fTJJ5+k/fbbr96OEwAAAKg+QQ0AYKkzderUdMghh6Qbb7wxrbDCCsX1kydPTjfffHO67LLL0g9/+MO05ZZbpltvvTU9//zz6YUXXqjXYwYAAAAWTlADAFjqRHmpPffcM/Xq1avC+rFjx6ZZs2ZVWL/BBhukTp06pTFjxlT5fDNmzEhTpkypsAAAAAB1r2k9vCYAQK25++670yuvvJLLT81r0qRJqXnz5mn55ZevsH7VVVfN26oydOjQNGTIkFo5XgAAAKD6ZGoAAEuNCRMmpOOPPz7deeedqWXLljX2vIMGDcqlqwpLvA4A0DBde+21ec6uNm3a5KVHjx7pT3/6U30fFgA0GIIaAMBSI8pLffbZZ2mLLbZITZs2zUtMBn7llVfm25GRMXPmzPT1119XeNynn36a2rdvX+XztmjRothxUVgAgIZpjTXWSBdccEFud7z88st5nq599tknvfnmm/V9aADQICg/BQAsNXbZZZf0z3/+s8K6fv365Xkzfvvb36aOHTumZs2apVGjRqX9998/bx83blwaP358HmUJALAwe++9d4X75513Xs7eeOGFF9LGG2/sAgJALRPUAACWGsstt1zq2rVrhXWtW7dOK620UnH94YcfngYOHJhWXHHFnHExYMCAHNDYdttt6+moAYBSNWfOnHTfffeladOmGSABAHVEUAMAaFAuv/zy1Lhx45ypMWPGjNSnT590zTXX1PdhAQAlJDJDY1DE9OnT07LLLpsefPDBtNFGG1W5f7Q5YimYMmVKHR0pACx9BDUAgKXa6NGjK9yPCcSHDx+eFwCAxdGlS5f02muvpcmTJ6f7778/HXbYYXker6oCG0OHDk1DhgxxsQGgBpgoHAAAAGARNG/ePK233nppyy23zAGLbt26pSuuuKLK/QcNGpQDIIVlwoQJrjcALCaZGgAAAADfw9y5cyuUl5pXixYt8gIAfH+CGgAAAADVFFkXu+++e+rUqVP65ptv0siRI3O5yyeeeMI1BIA6IKgBAAAAUE2fffZZOvTQQ9PEiRNT27Zt06abbpoDGrvuuqtrCAB1QFADAAAAoJpuvvlm1woA6pGJwgEAAAAAgJIgqAEAAAAAAJQEQQ0AoE589NFH6S9/+Uv68ssvXXEAAABgsQhqAAA17qSTTkonnHBC8f6DDz6YunTpknr37p3WX3/9NHbsWFcdAAAAWGSCGgBAjYsgxlZbbVW8f+qpp6Y99tgjvf7662mbbbZJp59+uqsOAAAA1E9Q49tvv03vvfdeKisrq4mnAwBK3MSJE1OnTp3y7ffffz+NGzcuBzK6du2aBgwYkF5++eX6PkQAAACgIQQ1LrnkkjRkyJDi/WeffTatvvrquaRElJOIjgsAoGFr27Zt+uyzz/LtJ598Mq244oppyy23zPdbtGiRvvvuu3o+QgAAAKBBBDVuuummtMYaaxTvDxw4MG288cbp4YcfTiuvvHIuLwEANGw77bRTOvPMM9Pw4cPThRdemPbdd9/itsjaKGRxAAAAACyKpou0d0ppwoQJab311su3P/744zzR59NPP5123HHHNHv27HT00Ucv6lMCAEuZyy+/PP385z9Pp5xyStpiiy3SeeedV9x2xx135HYDAAAAQK0HNVq1apWmTJmSb48aNSotu+yyabvttsv3l19++TR58uRFPggAYOkSpSmfeuqpSrc98cQTqWXLlnV+TAAAAEADDGpss8026YILLkiNGzdOF198cdp9991TkyZN8raYTyM6MQAAymd5xtKtW7fUunXr1KZNGxcHAAAAqLuJwidOnJj23nvvNHXq1ArlJO65555i1gYA0LDdcMMNebDDmmuumctNxVwa4cc//nG64oor6vvwAAAAgIYQ1Nhoo43SBx98kD7//PP04YcfFufXCJdeemkOegAADduwYcPSgAED0qGHHpr+/Oc/p7KysuK2nXfeOd133331enwAAABAAyk/VbDSSivlDorI2mjXrl1q2rRp2mSTTWr26ACAknTVVVelM844I51++ulpzpw5FbZ16dKlmLUBAAAAUKuZGoUJPrfddts8yWenTp3S66+/ntcfeeSR6c4771ycpwQAliIff/xxlSUpmzVrlktYAgAAANR6UOOuu+5Ke+yxR1p77bXTNddck+bOnVvctu6666Zbb711kQ8CAFi6xDwaL730UqXbXnzxxdS5c+c6PyYAAACgAQY1zjnnnHTCCSfk4Ebfvn0rbNt4443TG2+8UZPHBwCUoP79+6dzzz033XzzzWnKlCl53axZs9Kjjz6aLr744vTLX/6yvg8RAAAAaAhzasQk4ZGpUZnWrVunyZMn18RxAQAl7Ne//nUaP358Lk1ZCGBsv/32+ecxxxyTFwAAAIBaD2q0b98+vfPOO2mXXXaZb1vMrRHlJgAArrzyynT88cenv/zlL+m///1vWnHFFXP7Yf3113dxAAAAgLoJavz0pz9NZ511Vtpggw3SzjvvnNc1atQol5266KKL0tFHH714RwIALHVivq1YAAAAAOolqBEBjTfffDPtuuuuaaWVVsrrdt999/T555+nvfbaK51yyik1cmAAQGmbNm1aGjFiRHruuefSl19+mTM1dtxxx3TYYYflkpUAAAAAtT5RePPmzdPDDz+cRo0alScBPeKII/KE4U888URe37TpIsdJ0vDhw9Naa62VWrZsmbp3755eeumlBe4/bNiw1KVLl9SqVavUsWPHdOKJJ6bp06cv8usCADUnsjYLJkyYkDbddNP0q1/9Ko0bNy41btw4/4z73bp1y9sBAAAAFtWiRyD+fz179szL93XPPfekgQMHpuuuuy4HNCJg0adPn9zx0a5du/n2HzlyZM4GueWWW9J2222X/vWvf+WgSpTAuuyyy7738QAAiyc+vz/++ON8Oz7bw1tvvZUHIhTE53tkdp500knp3nvvdakBAACA2g9qlJWVpccee2y+chJRhiqCC4siAhGR8dGvX798P4Ibjz76aA5aVFbK6vnnn0/bb799ntsjRIbHwQcfnF588cXFORUAoIZMnDgxzZo1KzVr1iw9+eST6frrr68Q0Ahx/5xzzklHHXWU6w4AAADUTvmpTz/9tHj7q6++yhkSe++9d+6seOaZZ/LPGHUZwYavv/662i8+c+bMNHbs2NSrV6//HVDjxvn+mDFjKn1MvHY8plCi6oMPPsgBlj322KPK15kxY0aaMmVKhQUAqHkfffRR/jl79uxcJrIysX7OnDkuPwAAAFA7QY0ddtihePvXv/51ev/99/McGpGl8fbbb+efcT/Wx/bq+uKLL3KnxqqrrlphfdyfNGlSpY+JDI2zzz47H1OMBF133XXTzjvvnE499dQqX2fo0KGpbdu2xSXm4QAAatYKK6yQ2rRpk2/HQIdzzz03TZ48ucI+cf+8887L2wEAAABqJagRwYrCiMpHHnkkXXjhhWnXXXetsE/cj+BBTBZem0aPHp3OP//8dM0116RXXnklPfDAA7lcVZSyqMqgQYNyJ0phMTkpANS8u+66qzhQ4dJLL03vvfdeHkiw7777pl/+8pfpxz/+cb4f7YpLLrnErwAAAACovTk1xo8fn9Zee+00bdq0+TIrCtq3b5+3V9fKK6+cmjRpUqG8VYj78VyVOeOMM9LPf/7zdMQRR+T7m2yySX7NI488Mp122mm5fNW8WrRokRcAoPb07t27eLtr167p9ddfz3NnxRxcb775Zp6DK+bROvHEE9Maa6zhVwEAAADUTlCjdevWqWnT/7fr5ptvnq6++urUp0+fHJAomDt3brrqqqvSFltsUe0Xb968edpyyy3TqFGj8ijOwvPE/eOOO67Sx3z77bfzBS4KxxETmAMAS4YIXERQAwAAAKBOgxoRrCjMQxElpmIk5nrrrZf22WefnLXx2WefpYceeijPg/HnP/95kQ5g4MCB6bDDDktbbbVV2mabbdKwYcNy5kW/fv3y9kMPPTStvvrq+XVDTFAeHSQRXOnevXsubRHZG7G+fJAFAAAAAABogEGNvn37Fm/vtNNO6W9/+1ue5HPkyJHpq6++yuUkYuLuKP+0KJka4cADD0yff/55OvPMM3NQZLPNNkuPP/54scRVlL0qn5lx+umnp0aNGuWfH3/8cVpllVVyQCOOBwBYMnz33Xd5vqv7778//ec//0kzZsyYb5/CfF0AAAAANT6nRnlRMiom6K4pUWqqqnJTMTF4eVEGa/DgwXkBAJZMxx57bB78cPDBB6eNNtool5wEAAAAqJegBgDAgvzhD39Il1xySZWDFgAAAADqJKgRE3nfdNNNxXIS06dPr7A9SkO9//77i3UwAMDSIea56ty5c30fBgAAANDQgxq//e1v06WXXpp+8IMfpJ49eyonAQDM5+ijj0533HFH6t27t6sDAAAA1F9Q484770xDhgxJZ5xxRs0dBQBQ8i677LLi7datW6dnn302bbfddqlXr15p+eWXny+z88QTT6yHowQAAAAaVFAjyk1FBwUAQHm//vWv57sg48ePTy+88MJ86wU1AAAAgMXReFEfcMghh+TJPwEA5p13q7rLnDlzXDwAAACgdjI1HnjggeLtHj16pNNOOy19+umnadddd52vnETYb7/9Fv1IAAAAABZDWVlZuummm9KTTz6Zb0f5y/79+6fGjRd5LOdCDR06NPeTvPPOO6lVq1a5msWFF16YunTp4ncHAEtKUOP//u//5lv373//O91zzz2VlpMw+hIAGp5XXnllkfbfYostau1YAICG5Te/+U0ONOy///5p2rRp6ZRTTklvv/12GjZsWI2/1tNPP52OPfbYtPXWW6fZs2enU089NfXu3Tu99dZbeV4xAGAJCGp8+OGHtXwYAECp22qrrfLghoWJ0ZMGQQAAi+OTTz5JHTp0mG/9nXfemV599dXUvn37fL9nz57pmGOOqZWgxuOPP17h/ogRI1K7du3S2LFj00477VTjrwcALEZQY80116zObgBAA/bXv/61vg8BAFjKbbLJJjkr46STTkrNmjUrro8MiY8++qgY1IjqEnWVNTF58uT8c8UVV6yT1wOAhq5aQY0vv/xykZ7UBzkANDw/+MEP6vsQAICl3AsvvJBOPPHEdPPNN6fLL7887bXXXnl9lIDaeeed06abbpq+/fbbPN/FddddV+vHM3fu3HTCCSek7bffPnXt2rXK/WbMmJGXgilTptT6sQFAgw5qrLzyytUqJ1FgTg0AAACgpq2//vrpj3/8Y3r00UfTwIED0zXXXJOuuOKK9Itf/CLPcTF69Oi8XwQ4IqujtsXcGm+88UZ67rnnFjq5+JAhQ2r9eACgIahWUOOWW25ZpKAGANDwtGnTJpeg2nLLLdNyyy230LaDEYoAwOLac8898+Tcl112WerRo0cOapx55pl1EsgoOO6443KA5ZlnnklrrLHGAvcdNGhQDsKUbwd17NixDo4SABpoUKNv3761fyQAQEmL2tarrbZa8bYBEQBAbYo5NX7729+mQw89NJ188smpS5cuOSMi7temsrKyNGDAgPTggw/mzJC11157oY9p0aJFXgCAOgpqAAAszODBg4u3zzrrLBcMAKhxX3zxRc54+POf/5znqNhmm21ytsYdd9yRnn/++XT88cena6+9Nl199dU5e7S2Sk6NHDkyPfzwwzk7ddKkSXl927ZtU6tWrWrlNQGARQxqxERb8YEdk15FKueCRl7Gtn/84x/VeVoAAACAaotKEhMmTEhXXnllWmaZZdL111+fdtttt/TRRx+l7bbbLr300kvppptuyuWpYhLxuF3TImhSmLejvFtvvVWlCwBYUoIaMbqhdevWxdvKSQAAC3P33Xen++67L3c8TJ8+fb7tr7/+uosIACySZ599Nt1///1p1113zfe33377tNJKK6UPPvggTyIe/RX9+/dPBxxwQK1ljkb5KQBgCQ9qxGiDghEjRtTm8QAAS4FTTz01XXDBBXkwROfOnVPz5s3r+5AAgKVAVI+IUlPRxmjZsmXO1GjTpk3q1KlThf2WX375NGzYsHo7TgBgCZ1TI0YnRD3LlVdeWfYGAFB0yy23pLPPPjudfvrprgoAUGMKJZ4K/RDrrLNOzgw1CTcANByNF+dBMSFXpHjGBFjt27fPP+P+E088UfNHCACUpO7du9f3IQAAS5koMfW3v/0tffPNN3mQ5bvvvlssRQUANAyNF2dUxO67756aNWuWLr744nTXXXfln02bNk177LFHHpkJADRsRxxxRBo5cmR9HwYAsJSKeT9XWGGF+j4MAKAUyk9FKYlI9bz55psrrB8wYEDq169fOuecc9IvfvGLmjxGAKDERHvg+OOPz5mcu+yyS65rXV6UizjxxBNr5bWHDh2aHnjggfTOO+/kbNLtttsuXXjhhalLly7FfWLi8pNOOilPZj5jxozUp0+fdM0116RVV121Vo4JAAAAqKegxmeffZYOOuigSrcdfPDB6d57762J4wIASthTTz2VbrvttlwaYsyYMfNtr82gxtNPP52OPfbYtPXWW6fZs2fnSct79+6d3nrrrTyqM8RrP/roo7kGd9u2bdNxxx2X9ttvv1zOAgAAAFiKghrbbrtteuWVVyqtWRnrt9lmm5o6NgCgREVQYauttkpXXnll6ty5cy5bWVcef/zxCvdHjBiR2rVrl8aOHZt22mmnNHny5JxxGuWxfvjDHxbLa2644YbphRdeyG0dAAAAoISDGl9++WXx9vnnn58zMqJsw7777ps7CSJ748EHH0y33357nmMDAGjYJkyYkK666qq08cYb1/eh5CBGWHHFFfPPCG7MmjUr9erVq7jPBhtskDp16pSzSgQ1AAAAoMSDGiuvvHIuE1FQVlaWhgwZkufXKL8uRN3qOXPm1MaxAgAlYocddkjjxo2rNLOzLs2dOzedcMIJeW6Prl275nWTJk1KzZs3n2+ej5hPI7ZVJubdiKVgypQptXzkAAAAwGIHNW655ZYKQQ0AgAWJzM7DDjssBw8iI2LeAEL5zInaLoP1xhtvpOeee+57Tz4eAzoAAACAEghq9O3bt/aPBABYasQk3eGoo46qcmBEbWd2xuTff/zjH9MzzzyT1lhjjeL69u3bp5kzZ6avv/66QrDl008/zdsqM2jQoDRw4MAKmRodO3as1eMHAAAAamCicACAJTnLM0piDhgwIM/3NXr06LT22mtX2L7lllvmictHjRqV9t9//7wuSmWNHz8+9ejRo9LnbNGiRV4AAACA+iWoAQDUuPrM8oySUyNHjkwPP/xwWm655YrzZLRt2za1atUq/zz88MNz5kWUwGrTpk0OgkRAwyThAAAAsGQT1AAAlirXXntt/rnzzjtXWH/rrbcWgy2XX355aty4cc7UiAnA+/Tpk6655pp6OV4AAACg+gQ1AIClSpSfWpiWLVum4cOH5wUAAAAoHY3r+wAAAAAAAADqNKgxa9asmnoqAAAAAACA7xfUePnll9Pjjz9eYd3vfve7tNJKK6XWrVun3XbbLX322WeL8pQAAAAAAADVskhBjRNOOCGNHj26eP/f//536t+/f+rdu3e66KKL0ltvvZVOPvnkRXlKAKABkdkJAAAA1FlQ44033kg77rhj8f4DDzyQOnTokEaOHJkDHldeeWV68sknv9cBAQClTWYnAAAAUFuaVmennj175p9TpkxJgwcPTpdeemkqKytL7777bpoxY0baZZdd8vbvvvsuTZo0Kf3whz/M9/v27ZsOPfTQWjt4AGDJEwMddthhh1yWsnxm57777pu6d++eLrvsspzZOWLEiPo+VAAAAGBpDGr89a9/zT+XX375dNZZZ6W99torBzXWWGONdPHFF+fgRYjyU9ttt1166qmnaveoAYAlVmR2Dho0qNLMzkaNGqW11lorHXvssfV6jAAAAMBSHNQo6NGjRxo4cGD673//m5599tk0efLktMceexS3v/nmm2mdddapjeMEAJZwMjsBAACAJSqoEXNm7Lfffqlfv35pmWWWScOHD0/t2rUrbr/66qvTj370o9o4TgBgCSezEwAAAFiighrrr79++uc//5m++uqr1KZNm9SkSZMK22+//fYKQQ4AoOGR2QkAAADUlsaL86AVVlhhvoBGWHPNNdPs2bNr4rgAgBIVmZ0tWrTImZ133323zE4AAACgfjI1FuSzzz5Lw4YNS9dee23O5AAAGiaZnQAAAEC9BzVeeOGFdNttt6Xx48fnycB/9atf5U6LTz/9NJ199tnp1ltvTbNmzUoHHXRQrR0sAFA6IrOzMpHZ+c0339T58QAAAAANJKjxpz/9Ke29996prKwsrbLKKunJJ59Md911V7rjjjvSoYcemjMzDj744HTGGWekzp071/5RAwAlSWYn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AAAAlARBDQAAAAAAoCQIagAAAAAAACVBUAMAAAAAACgJghoAAAAAAEBJENQAAAAAAABKgqAGAAAAAABQEgQ1AAAAAACAkiCoAQAAAAAAlARBDQAAAAAAoCQIagAAAAAAACVBUAMAAACgms4777y03XbbpWWWWSYtv/zyrhsA1DFBDQAAAIBqmjlzZjrggAPS0Ucf7ZoBQD1oWh8vCgAAAFCKhgwZkn+OGDGivg8FABokmRoAAAAAAEBJkKkBAAAAUItmzJiRl4IpU6a43gCwmGRqAAAAAA3aKaeckho1arTA5Z133lns5x86dGhq27ZtcenYsWONHj8ANCQyNQAAAIAG7aSTTkp9+/Zd4D7rrLPOYj//oEGD0sCBAytkaghsAMDiEdQAAJYaH330UTrnnHPSU089lSZNmpQ6dOiQfvazn6XTTjstNW/evLjf66+/no499tj097//Pa2yyippwIAB6eSTT67XYwcA6k+0B2KpLS1atMgLALAUlZ8aPnx4WmuttVLLli1T9+7d00svvVTlvjfeeGPacccd0worrJCXXr16LXB/AKBhiLIQc+fOTddff31688030+WXX56uu+66dOqpp1YYGdm7d++05pprprFjx6aLL744nXXWWemGG26o12MHAErD+PHj02uvvZZ/zpkzJ9+OZerUqfV9aADQICwRmRr33HNPTsOMTocIaAwbNiz16dMnjRs3LrVr126+/UePHp0OPvjgtN122+UgyIUXXpg7J6LzYvXVV6+XcwAA6t9uu+2Wl/JlIqI9ce2116ZLLrkkr7vzzjvTzJkz0y233JKzNzbeeOPcEXHZZZelI488sh6PHgAoBWeeeWa67bbbivc333zz/POvf/1r2nnnnevxyACgYVgiMjWiE6F///6pX79+aaONNsrBjWWWWSZ3NlQmOiOOOeaYtNlmm6UNNtgg3XTTTXlU5qhRo+r82AGAJdvkyZPTiiuuWLw/ZsyYtNNOO1UoR1UYTPHVV1/V01ECAKVixIgRqaysbL5FQAMAGkhQI0ZKRumHKCFV0Lhx43w/Oh2q49tvv02zZs2q0GEBAPDee++lq666Kv3yl78sXoyYa2PVVVetcHEK92NbZWbMmJHLVpVfAAAAgAYY1Pjiiy9yDcrKOheq6liY129/+9s8EWj5wEh5OiIAoLSdcsopqVGjRgtcYj6N8j7+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kUESWRfls0IKYt6QyOC45ZZb8v34GfdjPUvHHDFlZWWVLgBA3RDUAAAAoFbF/AOvvfZansMiyjD169cv7b///sXtyy23XHrqqafSt99+m4YPH56zGiLj4dVXX63yOc8///xi4CKW8vNVxJwa8dinn346de7cOf3kJz+psYnJp0yZkvbcc888t0bM11GZmK/jvvvuS5MmTco/4z4AADXDnBoAAADUqtatW+eSUoXMhZjj4uabb06HH354cZ/I4Ih5K0aMGJGDG2PGjMnBkMjcqGwC55ioO4IVBR06dCjejvk4Yll//fXTtttum1ZYYYX04IMPpoMPPvh7nUeUyIo5PyIIE89XVfZFnMsGG2yQX2/DDTfMc3JEUAcAgO9PpgYAAAB1pnHjxunUU09Np59+evruu+8q3SeyIKKEVMxbUdVE3iuuuGIOlBSWeee2KCiUBpoxY8b3ztDo3bt3LmP1yCOP5FJaCxLZGaNHj5alAQBQwwQ1AAAAqFMxCXiTJk1yqanwyiuv5FJO48aNS7Nnz05ff/11uvjii3PgIAIc1fXBBx+koUOHprFjx+ZyVDEhebxWq1at0h577FHcLyZ6jsyJKA8VgZW4HcvMmTPz9o8//jhnWrz00ksVAhox8XhkmMT9eGwsc+bMqfRY+vfvnz7//PN0xBFHfM+rBQBAecpPAQAAUKciq+K4445LF110UTr66KPTaqutliZMmJBLO0VAIQIeUbYpylHFtuqKIMizzz6bhg0blr766qu06qqrpp122ikHN9q1a1fcLwINMd9Gweabb55/fvjhh2mttdZKs2bNygGWKINVCLrEfCChUEaroPCYys4xJj8HAKBmNSqLPNwGJkbVRH3VSGVu06ZNjT3van1H1thzsfSaOOKn9X0IlAjvKVSH95Slqy0BQMpzakSQYOedd3Y5WGppSwDAUlB+KtKOo+EaI2u6d+9eTPOtyn333ZfTgWP/mITtscceq7NjBQAAAACg9DzwwAO5rORKK62UGjVqlEtQLkxkcZ599tlp3XXXzf3R3bp1S48//niFfe68887UsWPHtMIKK6SBAwdW2PbRRx+lzp0756A2S0lQ45577sm/6MGDB+e03vij6NOnT/rss88q3T9Shw8++OB0+OGHp1dffTXtu+++eXnjjTfq/NgBAACoOX379pWlAQDUmpgja4cddkgXXnhhtR9z+umnp+uvvz5dddVV6a233kpHHXVU+vGPf5z7psMXX3yRy1tecskl6c9//nP63e9+l/74xz8WH3/MMcekCy64QKb/0hTUuOyyy/Ikav369cuTwF133XVpmWWWSbfcckul+19xxRW51upvfvObXGf1nHPOSVtssUW6+uqr6/zYAQAAAAAoDT//+c/TmWeemXr16lXtx9xxxx3p1FNPTXvssUdaZ5118pxgcfvSSy/N2z/44INcovjAAw9MW2+9derZs2d6++2387a77rorNWvWLO233361dk4NTb1PFD5z5sw0duzYNGjQoOK6xo0b5z+qMWPGVPqYWD9vCk9kdjz00EOV7j9jxoy8FET961DT6T5zZ/6/SeRgQaSZ4T2FUnhPWW655XIaLpUrTEnmPR0AtCMWh7YEQP375ptv8s+pU6cu9Lvd9OnT83t3+f2aNm2ann322bxu1VVXTd9++22+HyWoXnzxxRzg+Pe//51OO+20nLXh+2PN9UnUe1AjUnPmzJmTf/Hlxf133nmn0sdMmjSp0v1jfWWGDh2ahgwZMt/6+AODutb2rv4uOrDEv6eYALt6jV9tCQDQjlgc2hIAS44dd9yxWvsNGDAgL/OKDI2CnXbaqXh7//33L97eeOONv/dxNiSTJ09eYKmueg9q1IXIAimf2TF37tz05ZdfFieDoXZE9DE6eyZMmKBeHOA9pQRHRVC1Dh065M83GS21S1sC8H5SmrQjFk5bom5oSwD33ntvOuGEE4oX4v7770/bbbddvh1ZFJtuumnOroifC/Lhhx+mzTbbLFcYiv7ktddeO88BFnNnfPrpp5U+5rnnnstzcTz22GNp8803TzfffHMemP/DH/4wzyu9yiqr+AUtZlui3oMaK6+8cmrSpMl8v/y43759+0ofE+sXZf8WLVrkpbzll1/+ex871RNRtQVF1gAWhfcUlgTRkF1jjTXq+zAaDP/vAe8nLG20JeqWtgQ0XFECKoIPBauvvnpq1apVhY7zZZdddqF9lxHECBMnTkyzZs3KwelTTjklz69R2WNjKoSYDzrm4vjss89ypaKYgyN07tw5Tza+99571+i5NiT1PlF48+bN05ZbbplGjRpVIZMi7vfo0aPSx8T68vuHJ598ssr9AQAAAABoWCJwsd566xWXQkBjcbVs2TIHRmbPnp1+//vfp3322afS/c4999y02267pS222CIHNGL/ggiKxDoWX71naoQoDXXYYYelrbbaKm2zzTZp2LBhadq0aalfv355+6GHHpr/WGJujHD88cenH/zgB3l2+T333DPdfffd6eWXX0433HBDPZ8JAAAAAABLqpiWYPz48emTTz7J98eNG5d/RhWgQiWgefujo++5UIYqStudddZZeWD+ySefPN/zRxbGPffck1599dV8f4MNNsgZelF+Kp4/5pHeeuut6+x8l0ZNl5Q0oM8//zydeeaZebLvqE/2+OOPFycDjz+y+MUXRN2zkSNH5ppkp556alp//fXTQw89lLp27VqPZ8G8ouTX4MGD5yv9BbA4vKdAw+P/PeD9BNCWAGraI488UhxMHw466KD8M/oxI1hRWX90ZFbENArdu3fP5aqilFSUlpp3ioOysrJ05JFHpssuuyy1bt06r4vskBEjRqRjjz02l6W6+uqrc8CExdeoLK40AAAAAADAEq7e59QAAAAAAACoDkENAAAAAACgJAhqAAAAAAAAJUFQAwAAAAAAKAmCGizQ0KFD09Zbb52WW2651K5du7TvvvumcePGVdhn+vTp6dhjj00rrbRSWnbZZdP++++fPv300+L2f/zjH+nggw9OHTt2TK1atUobbrhhuuKKKyo8x3PPPZe23377/ByxzwYbbJAuv/xyvx1YitTV+0l5f/vb31LTpk3TZpttVqvnBlROOwKoSdoS0PBoSwCl+J5Snn6J2iGowQI9/fTT+T/yCy+8kJ588sk0a9as1Lt37zRt2rTiPieeeGL6wx/+kO677768/yeffJL222+/4vaxY8fmN4rf/e536c0330ynnXZaGjRoULr66quL+7Ru3Todd9xx6Zlnnklvv/12Ov300/Nyww03+A3BUqKu3k8Kvv7663TooYemXXbZpc7OEahIOwKoSdoS0PBoSwCl+J5SoF+i9jQqKysrq8XnZynz+eef5/+48Z96p512SpMnT06rrLJKGjlyZPq///u/vM8777yTo5RjxoxJ2267baXPE28gEbx46qmnqnyteMOIYMcdd9xRa+cDLL3vJwcddFBaf/31U5MmTdJDDz2UXnvttTo5L6Bq2hFATdKWgIZHWwIopfcU/RK1R6YGiyT+c4cVV1yxGJ2MqGavXr2K+0TpqE6dOuX/7At6nsJzVObVV19Nzz//fPrBD37gNwRLqdp8P7n11lvTBx98kAYPHlxrxw8sOu0IoCZpS0DDoy0BlMp7in6J2tW0lp+fpcjcuXPTCSeckOe+6Nq1a143adKk1Lx587T88stX2HfVVVfN2yoTwYp77rknPfroo/NtW2ONNXKUdPbs2emss85KRxxxRC2dDbC0vp+8++676ZRTTknPPvtsnk8DWDJoRwCl8p6iLQFLJm0JoFTeU7Qlap/eHqotUqneeOONPKn34orH77PPPnn0dNSsm1d0Qk6dOjXXtotOyfXWWy9PvgMsXWrr/WTOnDnppz/9aRoyZEjq3LlzDR4x8H1pRwA1SVsCGh5tCaAU3lP0S9SRmFMDFubYY48tW2ONNco++OCDCutHjRoVc7KUffXVVxXWd+rUqeyyyy6rsO7NN98sa9euXdmpp55arQt+zjnnlHXu3NkvB5Yytfl+Eo+N52jSpElxadSoUXFdvAZQ97QjgFJ5T9GWgCWTtgRQKu8p2hJ1w5waLCzolY477rj04IMP5slu1l577Qrbt9xyy9SsWbM0atSo4rpx48al8ePHpx49ehTXvfnmm6lnz57psMMOS+edd16108BmzJjhNwRLibp4P2nTpk365z//mScFLyxHHXVU6tKlS77dvXv3OjhToEA7AqhJ2hLQ8GhLAKX2nqJfom4oP8VCU7FGjhyZHn744bTccssV68e1bds2tWrVKv88/PDD08CBA/OEOPEfd8CAAfk/+rbbbltMxfrhD3+Y+vTpk/crPEeTJk3SKquskm8PHz48T7oTk++EZ555Jl1yySXpV7/6ld8QLCXq4v2kcePGxVqYBe3atUstW7acbz1Q+7QjgFJ7T9GWgCWLtgRQau8p2hJ1pI4yQihR8SdS2XLrrbcW9/nuu+/KjjnmmLIVVlihbJlllin78Y9/XDZx4sTi9sGDB1f6HGuuuWZxnyuvvLJs4403zo9v06ZN2eabb152zTXXlM2ZM6fOzxko7feTecVjunXr5tcK9UA7AijF95R5aUtA/dGWAErxPWVe2hI1r1H8U1cBFAAAAAAAgMVlTg0AAAAAAKAkCGoAAAAAAAAlQVADAAAAAAAoCYIaAAAAAABASRDUAAAAAAAASoKgBgAAAAAAUBIENQAAAAAAgJIgqAEAAAAAAJQEQQ0AAAAAAKAkCGoAAAAAAAAlQVADAAAAAAAoCYIaAAAAAABAKgX/H52Gji7ImmjNAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 1600x500 with 3 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "resumo_ano = df_analitico.groupby(\"ano\").agg(\n",
    "    receita = (\"total\",       \"sum\"),\n",
    "    lucro   = (\"lucro_total\", \"sum\"),\n",
    "    margem  = (\"margem_pct\",  \"mean\")\n",
    ").round(2)\n",
    "\n",
    "anos = [\"2023\", \"2024\"]\n",
    "fig, axes = plt.subplots(1, 3, figsize=(16, 5))\n",
    "\n",
    "axes[0].bar(anos, resumo_ano[\"receita\"] / 1e9,\n",
    "            color=[COR_NEUTRA, COR_NEUTRA], edgecolor=\"none\", width=0.5)\n",
    "axes[0].set_title(\"Receita Total\")\n",
    "axes[0].set_ylabel(\"R$ bilhões\")\n",
    "for i, v in enumerate(resumo_ano[\"receita\"]):\n",
    "    axes[0].text(i, v / 1e9 + 0.01, f\"R$ {v/1e9:.2f}B\", ha=\"center\", fontsize=10)\n",
    "\n",
    "cores_lucro = [COR_LUCRO if v >= 0 else COR_PREJ for v in resumo_ano[\"lucro\"]]\n",
    "axes[1].bar(anos, resumo_ano[\"lucro\"] / 1e6,\n",
    "            color=cores_lucro, edgecolor=\"none\", width=0.5)\n",
    "axes[1].axhline(0, color=\"black\", linewidth=0.8, linestyle=\"--\")\n",
    "axes[1].set_title(\"Lucro Total\")\n",
    "axes[1].set_ylabel(\"R$ milhões\")\n",
    "for i, v in enumerate(resumo_ano[\"lucro\"]):\n",
    "    offset = 1 if v >= 0 else -4\n",
    "    axes[1].text(i, v / 1e6 + offset, f\"R$ {v/1e6:.1f}M\", ha=\"center\", fontsize=10)\n",
    "\n",
    "cores_mg = [COR_LUCRO if v >= 0 else COR_PREJ for v in resumo_ano[\"margem\"]]\n",
    "axes[2].bar(anos, resumo_ano[\"margem\"],\n",
    "            color=cores_mg, edgecolor=\"none\", width=0.5)\n",
    "axes[2].axhline(0, color=\"black\", linewidth=0.8, linestyle=\"--\")\n",
    "axes[2].set_title(\"Margem Média\")\n",
    "axes[2].set_ylabel(\"%\")\n",
    "for i, v in enumerate(resumo_ano[\"margem\"]):\n",
    "    offset = 0.1 if v >= 0 else -0.5\n",
    "    axes[2].text(i, v + offset, f\"{v:.1f}%\", ha=\"center\", fontsize=10)\n",
    "\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e547df52-43ed-47f9-89d4-a45bca260482",
   "metadata": {},
   "source": [
    "## Análise 3 — Evolução mensal do lucro (2023–2024)\n",
    "\n",
    "A virada de janeiro de 2024 marca o momento em que o câmbio mais alto\n",
    "começou a impactar as margens mês a mês."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "6b1ba6e2-b072-475b-a317-2f9d7504159f",
   "metadata": {
    "jupyter": {
     "source_hidden": true
    }
   },
   "outputs": [
    {
     "data": {
      "image/png": "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xazff//dskNQ46233jKBoIzWUz9nGX1+y5YtawI16ZfL7mfQjq644grv+g4ePNg7X4NRnvnNmzfP9HuhQYMGF/we6Z06dcravHmz1a5dO+/yDRs2zFI7svs5za7jx4+neb1vvvnG+1i9evW888eMGZPp50+DHxf6Huro0aPeff7pp59O892dfj8HAAC4mBh+CgAAwE9kVCj8pZdeMo8FBgZKr169vMt+8MEH3r91GJejR4+av5s1ayZVqlQxfz/44IOydetW83fJkiXNsC1aYFaHc1E6ZMtdd90lCQkJud4WLfKtQ6Z42qXFcHW4ldmzZ8ujjz4qERER3mU7duxohpDRxxcvXmyGmNGi4VoUV7322muyb98+83diYqIZ8sYzvI8WGP7888/l3XffNcPaqB07dpj3y67u3btLVFSUGSJG33PNmjXy888/m8ceeuihTJ+nRcN1vZUOD6PDxGjbH3jgATMvLi7ODC2jw/VkRIfvefvtt+Wzzz7ztkELJus28dDtpnT99PUXLVpkiqrre1955ZVm/7iQ7XkhnnjiCe/zdX1ef/11815169bNdDicu+++Ww4cOGD+1qGDPvroI9PemjVrmnmHDh0y+6IOWZSfNm3aZIZM8vRVvXr1TDHqefPmmc+iZ33T2717t8TExJh+1L5/6qmn8v0zmBu2bNkia9euTbNvefgOK6WFu3353tch3S70PTz0cf0e0SLhOkydfucFBQVJ+/btzRBWWZHTz+n5fPLJJ96/9XNx3XXX5fq2Otd7eL6ntHD71VdfLcOGDbugdgAAAOSG4Fx5FQAAADieBjWefvppc9JdT2i/8MIL5mS2b4CjT58+3hPlX375pXe+nni+9dZbzd9NmjSRChUqyMmTJ82J5m+//Va6dOmSa+up6/fOO+9472sQQ8eF9/Csh0fr1q1lwoQJMnnyZHPyT0/0esaeVzrO/K+//iodOnQwJyH37Nlj5usJTj1BXLp0aXNfTyrrSU6ldTG0bSVKlMjyemsdj549e8rLL78sM2bM8L6Pvq6eeH7//fczbKueHPV4+OGHpWrVquZvfY72wd69e027NLigbU1P+8az/fWk5tChQ70ne31PYOqJ7/DwcKlWrZoJIOjfavTo0Re8PbNLgw6+J5H15L0GATz7Vbly5cx+5WvdunWyevVq733ddxs0aGD+rlGjhlx++eXm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AydISkoSN9u/f7/s2bNH3Gznzp2ybt06cbM///xTXn75ZXGrM2fOyOnTp/N7NYDzsiyLreQCHKPC7tx+fOoPx6gcn7oDx6hwCo5RkRXBWVoK8GNHjx6VqKgoCQwMND8adeo2egD+66+/SmJiolx66aXSoEEDcZsdO3bInDlz5ODBg3L11VdLhw4dxG02bdok9957r4wbN06aNm0qbrNmzRq5+eabZfr06VKmTBlxIw1mdOrUSdq3by9PPvmkxMTEiNusX79errzySjl16pRcc8010rhxY3GTzZs3y0svvSR//fWXNGnSRB5++GHX9ePff/8tCxYskJMnT5r/M2666SZxG+2/WbNmSXx8vNStW1fatWsn4eHh4hZHjhwx+2VAQID50ahTt9m1a5csWrRIYmNjpU6dOnL99deL23CM6nwcn7qD249ROT51B7cfo3J86g5uP0b1h+PTPGUByNTGjRutqKgo69lnn/XOO3PmjKu22Lp166wqVapYV1xxhVWhQgVz+/rrry03+f33361y5cpZ119/vXXNNddYAQEB1pdffmm5Ta9evUzbtD+XLVtmucnatWut8PBwq3///pZbbd261SpevLg1aNAgKzEx0XIj7ccCBQpY99xzj9W8eXNrxIgRrvpeXb9+vVWsWDGra9eu1oMPPmiFhIRYY8eOtdz2f0aJEiWsFi1amD4MDAy0unfvbq1YscJyC+3HIkWKWNddd53VtGlTKygoyOrSpYs1f/58yy3HNsHBwWm+T1NSUiy37acVK1Y0/+fXqFHDfBY/+OADy004RnU+jk/dwe3HqByfuoPbj1E5PnUHtx+j+sPxaV4jqAFkYteuXVb9+vWtatWqWTExMWn+03fLCbht27ZZZcuWtR5//HErNjbWfMk+8MADVufOna3jx4+74j+QzZs3m4DGsGHDrKSkJOvIkSNW27ZtrcmTJ1tuM23aNNOXffr0sYoWLWr9+OOPlhts2LDBioiIsIYOHWruJycnW2vWrLGWLl1qHnOLSZMmWXfeeaf5+/Tp09aUKVNMf77++utmP3a61atXm3584oknzP3BgwebIE5cXJy57/TvG/0Oveqqq8x3jceoUaOsgQMHmv50g0OHDll169b19qH69ttvTWCjQ4cO1qJFiyynO3HihPk/4qGHHvLO04BNw4YNrRtvvNGaM2eO5WS7d++2GjVq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",
      "text/plain": [
       "<Figure size 1600x500 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "df_analitico[\"mes\"] = df_analitico[\"sale_date\"].dt.to_period(\"M\")\n",
    "mensal = df_analitico.groupby(\"mes\").agg(\n",
    "    receita = (\"total\",       \"sum\"),\n",
    "    lucro   = (\"lucro_total\", \"sum\")\n",
    ").reset_index()\n",
    "mensal[\"mes_str\"] = mensal[\"mes\"].astype(str)\n",
    "\n",
    "fig, ax = plt.subplots(figsize=(16, 5))\n",
    "\n",
    "cores_bar = [COR_LUCRO if v >= 0 else COR_PREJ for v in mensal[\"lucro\"]]\n",
    "ax.bar(mensal[\"mes_str\"], mensal[\"lucro\"] / 1e6,\n",
    "       color=cores_bar, edgecolor=\"none\", width=0.7)\n",
    "ax.axhline(0, color=\"black\", linewidth=0.8, linestyle=\"--\")\n",
    "ax.set_title(\"Evolução Mensal do Lucro — 2023 e 2024\")\n",
    "ax.set_ylabel(\"Lucro (R$ milhões)\")\n",
    "ax.xaxis.set_tick_params(rotation=45)\n",
    "ax.yaxis.set_major_formatter(mt.FuncFormatter(fmt_milhoes))\n",
    "ax.axvline(x=11.5, color=\"gray\", linewidth=1, linestyle=\":\")\n",
    "ax.text(5.5,  mensal[\"lucro\"].max() / 1e6 * 0.88, \"2023\",\n",
    "        ha=\"center\", fontsize=12, color=\"gray\")\n",
    "ax.text(17.5, mensal[\"lucro\"].max() / 1e6 * 0.88, \"2024\",\n",
    "        ha=\"center\", fontsize=12, color=\"gray\")\n",
    "\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fd2f98fe-235a-49b9-bee7-49a3ac657eed",
   "metadata": {},
   "source": [
    "## Análise 4 — Lucro por categoria\n",
    "\n",
    "Propulsão representa a maior fatia do lucro absoluto,\n",
    "seguida de eletrônicos e ancoragem."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "6b1b9dbc-72b4-485e-b9d3-ec32594a75fd",
   "metadata": {
    "jupyter": {
     "source_hidden": true
    }
   },
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABQkAAAHqCAYAAACnYcjKAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjgsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvwVt1zgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAiKlJREFUeJzt3Qm4VeP7//H7NKd50KiJkqIZSfkqpQGVKSLqNBEihVSiCFFfFRrRSBnSgBBpRJMmlaFvg5TmaJ6H/b8+z/9a+7f2aZ+pznGG/X5d16qz11p77bXXWevsZ9/rfp47KhAIBAwAAAAAAABAxMqQ0jsAAAAAAAAAIGURJAQAAAAAAAAiHEFCAAAAAAAAIMIRJAQAAAAAAAAiHEFCAAAAAAAAIMIRJAQAAAAAAAAiHEFCAAAAAAAAIMIRJAQAAAAAAAAiHEFCAAAAAAAAIMJlSukdAAAAAADgfJ08edLeeOMNO3HihDVp0sRq1qzJwQSA80AmIQCkYn379rWoqCg3RUdHp/TuIBUoXbp08JyYN29eSu8OAAAprlOnTtarVy/btm2bXX311Ql+nvd5qmnz5s3B+XzW4kKofeadVzqXklPv3r3d62TMmNHWr1+f5NufPXt28L2MHj06ybeP1IcgIRDBxo0bF9I4igR169YNec/xTTpGiaH1FdjTtGrVqmR7H+nBP//8Y6+99prdeOONdvHFF1uWLFmsSJEids0117gGz7p1685722roe7+HIUOGJOl+AwDSf5tI08qVK89Z78svvzxnPW7YJIxudvqPW6FChVzmX0zPPPPMOcc4LoMHD7axY8da9+7d7d1333XBEiSd5cuXuyBsxYoVLXfu3JY9e3a79NJLXcamgkaHDx8+721Pnz492F7jOkq8v/76ywYNGuR+vueee6xcuXLBZStWrLBGjRpZgQIF3KSfNS+mZcuWWaZMmaxZs2ZhX6N+/frBzNznn3/ejhw5ch57irSE7sYAkMRfMubPn+9+1p3DqlWrcnzD0Jes1q1bu0Ch365du9ykBsvatWtd4/F8g4Qvvvii+7lUqVL25JNPppvfw6effmrHjx93P1eqVCmldwcA0q23337bxowZEzLvrbfeSrH9SW/27NljH3/8sWsPeI4ePZqobCWtr6DF+++/bw888ECS7RuftWanT5927adhw4adc3z++OMPN82cOdMFoG6//fbzOs5q540fPz7kZn56UK1aNfv+++/dz9myZUu21xkwYIAdO3bM/dy5c+fg/O3bt1uDBg1s//79weOr6+ynn35y7etixYoFf8cdO3a0iy66yIYPHx7r62jbS5YssR07drhAfHpqV+NcBAkBpHq6Q5kzZ84ka/AfOHAg+Pjrr7+2V199NfjY+0D3XH755UnyupHi7NmzLitAd5ljozvFd9xxh506dco9Llq0qHXp0sVq1KjhGitr1qyxSZMm/Yt7nbaug8R0owIAnL8PP/zQBg4c6IIg8vvvv9usWbPSZPsntVK7zB8kVLBv3759CX6+ghvqfZDU0vtnbULOrUcffdQFhDw33XSTywa95JJL7O+//3ZtZv2+8H/Utg0EApYnTx6rU6dOsh4aBce9AKBuiF9//fUhN+N1HVWuXNkefPBBN09/y9TG/uqrr6xDhw5unrIQ1fNJ16F+r7FREFhtewUkR40aRZAwvQsAiFhjx44N6M+AN8Vl7ty5wfVKlSoVsqxPnz7BZW3atAlZdubMmcC4ceMC9evXDxQoUCCQOXPmQKFChQI33XRT4Isvvgiud+ONNwa3MWbMmMDgwYMDV1xxhVu/S5cuwfVWrVoVePDBBwMlS5YMZMmSJZArV67ANddcExg4cGDg+PHjSX4MTpw4ERgyZEjguuuuC+TOndvtzyWXXBK47777AsuWLYt1OzEn77j89NNPgVatWgWuuuqqQMGCBQOZMmUK5MyZM1ClSpXACy+8EDh06FCCj204f/zxR8jr/v3334FOnToFChcuHMiaNWugRo0agc8+++yc5509e9a9h7p16wby5cvn9kvPadasWeC77747Z33/a/z888+BJ554IlCsWLFAhgwZAtOmTYt1/3Q+6PfqP5d27twZdt01a9YEf/7mm28CLVq0CJQvXz6QP39+t3/6fVx77bWBN954I3Dy5MngutpmXL8LHSPPkiVLAi1btnS/U/1u8+bN687VcMdIpkyZEqhatao7lnpOjx49Ar/99luc59D8+fMDd955Z6Bo0aLB16hTp07g3XffdcfDLyHXgf/96br0TJo0yf2+LrvsskCePHncMdKx+s9//hMYPXq0+x0DAMLzf45nz57d/Q3Vz/379w+u8+ijj7p5+vzx/933/y1OzOeV6LPd244+899///3g50zz5s0v6PMnMZ9xMT9/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Qg8ePMiAoQAAAKkYbTYAAJCWESRMAw4dOmR58uRx/wMAACB1os0GAADSMoKEAAAAAAAAQIQjSAgAAAAAAIAUceLECevYsaOVKVPGcuXKZVdccYWNGTMm7Lq7d++2Vq1a2SWXXGK5c+e2atWq2eeffx5cfubMGXvwwQctb968VqdOHdu+fXtw2cKFC61u3boM5RYHgoQAAAAAAABIEadPn7aiRYvad9995+oxjBs3zp566in79ttvz1n38OHDLjC4ePFi279/v7300kt233332a+//uqWT5061TZv3my7du2ymjVrWv/+/d38U6dO2eOPP24jR460qKiof/09phUECQEAAAAAAJAicuTI4YJ9l112mQvgXXfddVavXj374Ycfzln30ksvtaefftplEmbIkMGaNm1q5cuXd0FD2bRpk8sgzJo1q9188822ceNGN3/gwIFuXWUpInYECQEAAAAAAJAqHD9+3JYuXWqVK1eOd111P/7tt9+C61aqVMm+//57O3bsmM2ePds93rBhg02ePNl69uz5L+x92kaQEAAAAAAAACkuEAhYhw4drFy5cnbnnXfGue7JkyetZcuWds8999jVV1/t5t1yyy1u3EF1Nd62bZv16NHDHn30UXvzzTdtxowZblmTJk1cYBHnyhRmHnBeoqOj3dgBAAAAAAAAiQ0QKqC3bt06Nz6huhPHFSC8++677aKLLrJ33303ZNnLL7/sJnn//fetZMmSdtVVV7lswzVr1tjPP/9s7dq1s0WLFvELioFMQsRJUXb15c+ZM6flz5/fbrzxRlu2bNkFVS3SNgsVKuQqEWk8gHfeeSdkHY1BoAtdr6mpSpUq8f5hKF26tHve9OnTQ5a/+uqrwe1o0lgHWk+DmSZkeUw7duywZs2aWbFixdx6q1atClm+du1aa9SokRUsWNAt10CqfnPnznVjK+TJk8dVWwIAAAAAINIpQPjYY4/ZkiVLXMESfWeOKw7QokUL9/+UKVMsS5YsYdf7+++/7fXXX3fjEa5fv95KlChh+fLls1q1arlAIc5FkBDx0kWlCkI7d+50KbsxU34nTJhgFSpUsA8//NAF/xRI3LdvX9htZcqUyd5++21XhlxVixSMe/75592YAX4qTa7X1BTfxatBSXV3QAOXxtSrV6/gdjRpX/XHRunFCVkek+5kNG7c+JxgpCdz5swu1Tm2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0l0X40mTJtlnn31muXLlCo4rmCdPHjdenrRu3dqKFy/uugxLly5d3Dh6b7zxht1666320Ucf2bJly+ydd95J0fcCAADwbyGTEAAAAOnKiBEjXPdfjWtXtGjR4PTxxx8H19myZYvt2LEj+FhFNBRYVFCwSpUq9umnn9r06dPjLHYCAACQnpBJCAAAgHTX3Tg+qqAbU4sWLdwEAAAQicgkBAAAAAAAACIcQUIAAAAAAAAgwhEkBAAAAAAAACIcYxICAAAAaUjJsd1Tehfgs6XtAI4HACBdIJMQAAAAAAAAiHAECQEAAAAAAIAIl+aChOPGjbN58+al9G4AAAAAAAAA6UaKBwmjo6MtKirKTZkzZ7YyZcpY9+7d7fjx4xe87b59+9oVV1xhOXLksHz58lmDBg1syZIlIev8888/1qpVK8udO7flzZvX2rdvb4cPH45zu9q3xx57zAoUKGA5c+a0u+66y3bt2hVcvnnzZvd+MmbMaNu2bQt57o4dOyxTpkxuudYDAAAAAAAALNKDhNK4cWMXPNu0aZMNHjzYRo0aZX369AlZZ+7cuVa7dm3r0qWL3XHHHVa9enUbMWJEnNu9/PLLbejQobZmzRr74YcfrHTp0tawYUPbs2dPcB0FCH/55RebNWuWzZgxwxYsWGAPPfRQnNvt2rWrffHFFzZ58mSbP3++bd++3e68885z1itevLhNmDAhZN748ePdfAAAAAAAACC1SBVBwqxZs1qRIkWsRIkSdvvtt7uMPwXtPPv377fmzZvblVdeaU8//bQNHDjQevbsGe9277//fretSy+91D130KBBdvDgQVu9erVb/ttvv9nMmTPtvffes5o1a1qdOnXs7bffto8++sgF/sI5cOCAjR492m3rpptusho1atjYsWNt4cKFtnjx4pB127Rp45b56bHmAwAAAAAAAKlFqggS+q1du9YF3LJkyRKct2HDBjt06JDLLlQgsWzZstaiRQt75JFHErzdkydP2jvvvGN58uSxKlWquHmLFi1yXYyvvvrq4HoKKmbIkOGcbsme5cuX26lTp9x6HnVpLlmypNueX7NmzWzfvn0ui1H0vx43bdo0zn09ceKEC2b6JwAAAAAAACBdBwnVzVdj+2XLls0qVapku3fvtmeeeSa4vHz58lawYEHr0aOHrV+//ry3ra7MylDUtmTnzp1WqFChkPU1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uSlz5sxWpkwZ6969ux0/ftwuhIqpPPvss1apUiUXuCxWrJi1bt3atm/fHrKegpytWrWy3LlzW968ea19+/Z2+PDhOLetfXvsscesQIECljNnTrvrrrts165dweWbN2927ydjxoy2bdu2kOfu2LHDMmXK5JZrPQAAAAAAACBNBAkbNWoU/Llbt27u/19//dVWrFhhX3/9tfv/l19+cYGvp556KtE70bhxYxc827Rpkw0ePNhGjRplffr0CVln7ty5rkCKxkK84447rHr16jZixIhYt3n06FG3X88//7z7f+rUqS6Y2axZs5D1FCDUvs+aNctmzJhhCxYscEVZ4tK1a1f74osvbPLkyTZ//nwXeLzzzjvPWa948eI2YcKEkHnjx4938wEAAAAAAIA01d1YATxl5inTT8E0BfHKly8fso4e9+vXzzp16pTonciaNasVKVLE/VyiRAlr0KCBe53XX3/dzdu/f781b97cWrZs6QKKRYsWtTx58tjevXtj3aaWaxt+Q4cOtWuvvdZVZy5ZsqT99ttvNnPmTPvpp5/s6quvduu8/fbbdsstt9h///tfl30Y04EDB2z06NE2adIku+mmm9y8sWPHWoUKFWzx4sV23XXXBddV92st69mzZ3CeHmu+jhUAAAAAAACQZjIJxesae/r0acuePXvYdTT/zJkzF7RD6tq8cOFCy5IlS3Dehg0b7NChQy67UEHEsmXLWosWLeyRRx5J1LYV4FO2o7oVy6JFi9zPXoBQFKBUF+olS5aE3cby5ctdwFTrea644goXdNT2/JS1uG/fPjd2o+h/PW7atGmi9hsAAAAAAABI8SBhvnz53Jh9oi6/L7/8sgu4+enxK6+84pYnlrr5amy/bNmyuTEEd+/ebc8880xIlmLBggWtR48etn79ejsfGkdQYxTed999wfeyc+dOK1SoUMh6Gi9QhVi0LBzNVwDTCzR6ChcufM5zlHn5wAMP2JgxY9xj/a/Hmh+XEydO2MGDB0MmAAAAAAAAIEWDhB9++KELgskbb7zhMvuU0Xf77bfbww8/7MYI1OONGze6brqJVa9ePVu1apXL3lNX3LZt27piIJ5cuXLZnDlz3DiDw4YNc5l4ytJbuXJlgravzL977rnHAoFAnOMYJod27dq5sQsVQNT/ehyf/v37u+7S3qRjCwAAAAAAAKRokLBhw4bBn6+6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IiXhMC4hAAAAAAAAkI6DhGPGjIk1OAgAAAAAAAAgAoKE0dHRybMnAAAAAAAAANJG4RIAAAAAAAAA6QtBQgAAAAAAACDCESQEAAAAAAAAIhxBQgAAAAAAACDCESQEAAAAAAAAIlySBQlPnTqVVJsCAAAAAAAAkFqDhMuWLbOZM2eGzPvggw+sQIECliNHDmvcuLHt3r07qfcRAAAAAAAAQGoJEj755JM2b9684OM///zTOnbsaA0bNrQBAwbYr7/+at27d0+O/QQAAAAAAACQGoKEa9eutRtuuCH4eOrUqVasWDGbNGmSCyC+9dZbNmvWrOTYTwAAACBBFixYYE2bNnXt1KioKJs+fXq8z9GN8OrVq1vWrFmtbNmyNm7cOI42AACIKJkSslK9evXc/wcPHrQ+ffrYG2+8YYFAwNavX28nTpyw+vXru+XHjh2znTt32k033eQeR0dHW+vWrZNz/wEAAIAQR44csSpVqli7du3szjvvjPfo/PHHH3brrbdap06dbOLEiTZ79mzr0KGDFS1a1Bo1asTRBQAAESFBQcK5c+e6//PmzWt9+/a12267zQUJL7nkEhs4cKALBoq6G19//fU2Z86c5N1rAAAAIBZNmjRxU0KNHDnSypQp426ES4UKFeyHH36wwYMHEyQEAAARI0FBQk+tWrWsW7du9vfff9v3339vBw4csFtuuSW4/JdffrFLL700OfYTAAAASBaLFi2yBg0ahMxTBqGG04mLetRo8qjXDQAAQESMSagxBzVOS9u2be2jjz6yYcOGWaFChYLLhw4das2aNUuO/QQAAACShYbLKVy4cMg8PVbQT8PpxKZ///6WJ0+e4FSiRAl+QwAAIDIyCcuVK2dr1qyxffv2We7cuS1jxowhyydMmBASNAQAAADSq549e7peNh4FFQkUAgCAiAgSevLlyxd2fqlSpezQoUMXuk8AAADAv6ZIkSK2a9eukHl6rJvi2bNnj/V56mGjCQAAIOK6G8dl9+7d1qtXLytZsmRSbRIAAABIdhp3WxWN/WbNmuXmAwAARIoEBwkXL15sjzzyiN166632+OOP2/r164N3WR977DErXbq0q3SsysfJady4cTZv3rxkfQ0AAACkXYcPH7ZVq1a5Sf744w/385YtW4LdhFu3bh1cv1OnTrZp0ybr3r27/f777zZ8+HD75JNPrGvXrin2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WbNmVqxYMbf+qlWrzllH2yhXrpxddNFFVqdOHfv999/DbqtXr17xvmaTJk3csfCmbNmyufexd+9et3zu3LlWr149y5Mnj+XNm/ec5x88eNDatGljhQoVcsezcePGtnHjxjjfIwAAAADgwhAkBIAk8Prrr9vhw4dt586dVrNmTbvzzjtDlk+YMMEqVKhgH374oQt+KZC4b9++WLdXpUoVGz58uF177bVhlyuQ9/7779sll1wS774pQKdAW2yBvXXr1lmrVq1s8ODB9s8//9hNN91kzZs3t9OnT4es9/PPP9sXX3xhRYsWjfP1vv76a3csvKljx47WoEEDK1iwoFueI0cOa9eunQ0aNCjs81944QW3T7/++qsLcCoY+sADD8T7PgEAAAAA548gIQAkoSxZsrgsuK1bt9qePXvcvG3btgWDYvfdd5/9+eef1rt3b8uUKVOs23nsscesfv36Lgsv3Gs8+eSTdsMNN1jGjBnj3afChQvbo48+GmvA8YMPPnCZfbfddpt7veeff952795t33//fXCdM2fOWIcOHWzo0KHu9RPq+PHjNnHiRGvfvn1wnvbjwQcftMsuuyzsczZt2uQyHxVUVIam1l2zZk2CXxMAAAAAkHgECQEgCR07dsxGjx7tAlz58uVz89TNVl10a9eu7R5nz57dbr75ZsuVK1eqOParV6+2qlWrBh9nzpzZKlas6OZ7lGVYuXJllwGZGNOmTXOZjHfccUeCn9O5c2f75ptvXFamjue4ceOsadOmiXpdAAAAAEDixJ7GAgBIsJ49e1rfvn3deHrqTjx16tRgpmClSpVclp7+V8Bs/Pjxduuttwa736Y0dQmOOTagHh86dCiY2acMwhUrViR62++9957LBExM9qG6Wmu8QnVrVqakxkqcNWtWol8bAAAAAJBwZBICQBLo37+/7d+/33UzLl68eEgWngKDyqjTpGWffPKJlS1b1hYtWpQqjr2Kixw4cCBknh57mY4qovLyyy+7IiKJ8ccff7giJf6uxgmhoiy5c+d24yMePXrUOnXq5LpW62cAAAAAQPIgSAgASUhBwHfffdeeffZZ2759e8iy6tWru+Dgl19+aS1atLB33nknVRx7dSP2Vzw+deqUKxqizEeZPXu2GwNRmY+aFAht3bq1de3aNc7tqtu1xh+86qqrErU/K1eudIFBdddWBuITTzxh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a5flyZPHHnjggeDy7du320033eT2SfumIORjjz0WXP7CCy/YunXrXCBRy0qXLh3yfAAAACApECQEAAApJkuWLC5LbuvWrbZnzx43b9u2bdauXTsbNGiQ3Xffffbnn39a7969LVOmTLFuR0G1+vXrW7Zs2eJ9zb/++ssCgYC1atXKZQIqwHjNNdfYmjVr3PImTZpYy5YtLW/evG7/nnnmGbd/2g8pXLiwPfroowkKSMq0adPsiSeesOLFi1v27NldQHLWrFm2efNmt1xZjAoSKntQy5VlWb169eDzN23a5DIXldmoZQ8++GBwXwEAAICkQpAQAACkmGPHjtno0aNdACxfvnxu3t69e13wrnbt2u6xAmc333yz64qbFKpWreoyE8ePH++yA1esWGE///yzNWzYMOz68+fPdwHDkiVLntfrnT171gUl/Y9l9erVwe2r67Xeb4ECBeyGG26wJUuWBNfv3Lmzy3JUVqOO17hx46xp06bntS8AAABAbAgSAgCAf13Pnj1d4C1Hjhw2adIkmzp1ajBTsFKlSnbbbbe5/xVAUzBPgcOkou7CKojStWtXl5l39dVX29NPP+3GKIxpy5Yt9vDDD9sbb7wRZyZjXG699VZ788033bbUxVrdhxUE1ViD8s8//7hu1QMGDHDdie+99173/r3u1cp0VBflokWLukDpDz/84LowAwAAAEmJICEAAPjX9e/f3/bv3++68aobrpdV5wXx1EVXk5Z98sknVrZsWVu0aFGSvPacOXOsU6dOLjB58uRJW79+vU2cONFGjBhxTrdkdWFWJp+6P19IQLRBgwYuQ/Dyyy93mYzKHFTWoOjn22+/3WUSqnuzXk/dpr33e/fdd7uCJwomHj161O27tqWfAQAAgKRCkBAAAKQYBQHfffddV0REBTz8NC6fgoMq+tGiRQt75513kuQ11b1YxVJUZVkBycsuu8wF4vQ6/gBhvXr1XIGQXr16XdDrKeCn8RU1pqHe4y233OKCk9oHL1MwLitXrnSBQXXHVhBR4xtq//wVlwEAAIALRZAQAACkKAUDFbB79dVX3WNl9n311VfBsfuOHDni5qm7bWwUdDt+/Lh7zunTp93P+j+cWrVq2U8//WQ//vijGytQwbspU6ZYtWrV3HIF8hQgVLffPn36hN2Gtq8p5muHoy7Eeg29lt6HCpR069bN8ufP75Z3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em+++aYrCgUAQGpEmw2pFW02AGlNppTeAUS2kydPWpYsWSw1evXVV4M/v/baaym6L0BinTlzxmUoZsiQwb788svg/BUrViR6W3ny5OEXgIihoZp1/WTKRBMJ8KPNBiQP2mzA+aHNljzIJESSqlu3rnXu3NlNCiwoC+/55593F7B3N61fv37WunVry507tz300ENu/pQpU+zKK6+0rFmzunXeeOONkO16z7vvvvssR44cVrx4cRs2bFhw+ebNm11AZNWqVcF56r6peeoaEM6ff/5pTZs2tXz58rlt6vW/+uqr4Id1+/btrUyZMpY9e3YrX768y6byO3v2rL300kt2ySWXuP2uWrWqzZw5MwmPJtILnSv9+/cPnk9VqlSxTz/9NNb1f/jhB7vhhhvcuiVKlLAnnnjCjhw5ErzGdO527drVnd+aRJl+efPmddkUFStWdOfkli1bbN++fe5603l+0UUXWZMmTWz9+vXB1/Ke980331iFChUsZ86c1rhxY9uxY0es3Y31fgYMGGBly5Z1r1OyZEl75ZVXgsvXrFljN910k9t/ddnXde7PXtQ1ee2117rrTq9du3Zt954QmfR3s06dOu5c0Ply22232caNG0P+tk+dOtXq1avnzmFdP4sWLQrZxo8//uiuDS3Xud6oUSN37suJEyfcNVSoUCHLli2be62ffvrpnO5jGgOqRo0a7pzWNah9aN68uRUuXNhdF9dcc4199913Ia+r60RDUehc1/U9adKkc7JG9FmkYSsuvvhi97mna+Pnn38OLu/bt6/7/BgzZoy7lvRajz76qPsc0nVWpEgRt+/+awxICrTZaLPhXLTZaLMhdrTZ+kZGm03VjYGkcuONNwZy5swZ6NKlS+D3338PfPDBB4GLLroo8M4777jlpUqVCuTOnTvw3//+N7BhwwY3LVu2LJAhQ4bASy+9FFi3bl1g7NixgezZs7v/PXperly5Av3793frvPXWW4GMGTMGvv32W7f8jz/+UBQysHLlyuBz9u3b5+bNnTvXPdb/eqz5cuuttwZuvvnmwOrVqwMbN24MfPHFF4H58+e7ZSdPngy88MILgZ9++imwadOm4Pv4+OOPg9sfNGiQey8ffvihe6/du3cPZM6cOfC///2PEwohXn755cAVV1wRmDlzpjvXdG5nzZo1MG/evHPOS10TOXLkCAwePNidSz/++GOgWrVqgejoaLf877//DlxyySXuetmxY4ebRNvU+Xf99de75+icPHLkSKBZs2aBChUqBBYsWBBYtWpVoFGjRoGyZcu6c9z/vAYNGrjzffny5W79+++/P7j/bdq0CTRv3jz4WOd6vnz5AuPGjXP7+/333wfeffddt+zw4cOBokWLBu68887AmjVrArNnzw6UKVPGbUNOnToVyJMnT+Dpp592z/3111/ddv7880/Omgj16aefBqZMmRJYv369+xvetGnTQKVKlQJnzpwJ/m3X9TNjxgz39//uu+92nwk6l0TP0fX0yCOPuHN87dq1gbfffjuwZ88et/yJJ54IFCtWLPDVV18FfvnlF3cu6vzVtSTeNVi5cmX3maLzUsu0rZEjR7rzWNdi7969A9myZQs5V3XdVK1aNbB48WJ37egzUJ9fun796+g96frSdp566qlAgQIFgq/fp08f97mp96X9+/zzzwNZsmRx1+rjjz/uruUxY8a4fdTrAEmFNhttNpyLNhttNsSONlufiGizESREkjc4FWA4e/ZscN6zzz7r5om+2N1+++0hz1EwQsE6v2eeeSZQsWLF4GM9r3HjxiHr3HvvvYEmTZqcd5BQX0L79u2b4Pf22GOPBe66667gY33pfOWVV0LWueaaawKPPvpogreJ9O/48eMuwLxw4cKQ+e3btw/cd99955yXmv/QQw+FrKsgnALpx44dC14P/iCEF+zTdhTY8CggoXkKGnr27t3rghiffPJJyPMUGPEMGzYsULhw4bBBwoMHD7qAjBcUjEk3BBSAUbDQ8+WXX7r937lzpwuM6PUUIAXCUXBP54iCc97f9vfeey+4XI0yzfvtt9/cY11HtWvXDrstnYcKgk+cODE4TwFy/f0eMGCAe+xdg9OnT4/3F3LllVe6AKTo9fU8Bf88CnRqnnd96trVzST9HfC77LLLAqNGjQoGCfU3QteWR43N0qVLu0Cpp3z58u5GGZBUaLPRZkMo2my02ZA4tNkC6bLNRndjJLnrrrsu2AVSatWq5bo3Kg1Xrr766pD1VTlY3Q399Nj/HG87fnqs554vdT97+eWX3Wv16dPHVq9eHbJc3ZnV9UxdxJRK/M4777jum3Lw4EHbvn172P2+kH1C+rNhwwY7evSo3Xzzze488qYJEyYEu1T6qRuiugD711XXSXV/+eOPP+J8LY3vWbly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",
      "text/plain": [
       "<Figure size 1300x500 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "cat = df_analitico.groupby(\"actual_category\").agg(\n",
    "    lucro  = (\"lucro_total\", \"sum\"),\n",
    "    margem = (\"margem_pct\",  \"mean\"),\n",
    ").round(2).sort_values(\"lucro\", ascending=False)\n",
    "\n",
    "cores_cat = [COR_LUCRO, COR_NEUTRA, COR_PREJ]\n",
    "fig, axes = plt.subplots(1, 2, figsize=(13, 5))\n",
    "\n",
    "bars = axes[0].bar(cat.index, cat[\"lucro\"] / 1e6,\n",
    "                   color=cores_cat, edgecolor=\"none\", width=0.5)\n",
    "axes[0].set_title(\"Lucro Total por Categoria\")\n",
    "axes[0].set_ylabel(\"R$ milhões\")\n",
    "axes[0].yaxis.set_major_formatter(mt.FuncFormatter(fmt_milhoes))\n",
    "for bar, val in zip(bars, cat[\"lucro\"]):\n",
    "    axes[0].text(bar.get_x() + bar.get_width() / 2, val / 1e6 + 0.3,\n",
    "                 fmt_brl(val), ha=\"center\", fontsize=9)\n",
    "\n",
    "bars2 = axes[1].bar(cat.index, cat[\"margem\"],\n",
    "                    color=cores_cat, edgecolor=\"none\", width=0.5)\n",
    "axes[1].set_title(\"Margem Média por Categoria (%)\")\n",
    "axes[1].set_ylabel(\"%\")\n",
    "axes[1].axhline(0, color=\"black\", linewidth=0.8, linestyle=\"--\")\n",
    "for bar, val in zip(bars2, cat[\"margem\"]):\n",
    "    axes[1].text(bar.get_x() + bar.get_width() / 2, val + 0.05,\n",
    "                 f\"{val:.1f}%\", ha=\"center\", fontsize=9)\n",
    "\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "51739eb7-4e29-4e61-a3c9-82a794e24fe9",
   "metadata": {},
   "source": [
    "## Análise 5 — Top 10 clientes por lucro gerado\n",
    "\n",
    "Os 10 principais clientes concentram parcela significativa do lucro total,\n",
    "reforçando a importância de estratégias de retenção para esse grupo."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "5fa96b35-e347-478b-aac3-a059ee8c602f",
   "metadata": {
    "jupyter": {
     "source_hidden": true
    }
   },
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABKcAAAJOCAYAAABiG2QNAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjgsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvwVt1zgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAxcJJREFUeJzs3QW4VNUfr/EFIigiKCp2oGIjFgYGdneDXYhidyt2i/HHwEBsTAxsQezuLkwwEezAc5933bvm7jPMzEnYHHg/zzMPnIlds2fPrO/+rbWbVVVVVQVJkiRJkiQpB83zmKkkSZIkSZIEwylJkiRJkiTlxnBKkiRJkiRJuTGckiRJkiRJUm4MpyRJkiRJkpQbwylJkiRJkiTlxnBKkiRJkiRJuTGckiRJkiRJUm4MpyRJkiRJkpQbwylJkqTJwO677x6aNWsWb6ecckrhfv6f7uc5kiafz6ckqXEYTkmSpFpbYIEFCg202tyGDx+e29YdMWJE2G+//cIKK6wQWrVqVVimNddcs+xrqqqqwvXXXx9WW2210K5du9C6deuw1FJLhVNPPTX89ttvdV6Gn376KZx99tmhe/fuYbbZZgstW7YMc8wxR+jatWs44YQTwgcffBAmdzTE0+3nn3/Oe3GaBPb77Odg5MiRYWrzzjvvhEMOOSQst9xyoX379nHfn3322UPnzp3DrrvuGgYPHhx+//33vBdTkjSZaJH3AkiSJE0Md911V7jiiivqXB0xaNCgCRrZJ598crjnnnvCsGHDYmhVGw888EBshBNQZX377bfx9vLLL4e33347TreSPffcM6y77rrx/zTuJ7W+fftW2z4zzTTTJF8GNR3jx48PRx99dLjwwgtj2Jv13XffxRv7/Q033BAefPDBsOGGG+a2rJKkyYfhlCRJqrU77rgj/Pnnn4W/r7322nDdddfF/1MRdPvtt1d7PlUSeenQoUPYfPPNY+XUW2+9NcGyFbvxxhsLwdT0008fzj///FjtRIXThx9+GF577bVw1FFHhSuvvLJWlTNbbbVV+Oeff+Lfc845Zzj44IPD8ssvH/7999+4PDfffHOt1mO++eaLN00+fv3119CmTZvQ1E2M9TjooINC//79C3/z+dtrr71Cp06d4r7/ySefhMcffzyGtxMLnzuCMaq1JElNRJUkSVI9nXzyyZRGxNv8888/wePjxo2rOvXUU6uWXXbZqjZt2lS1bNmyqmPHjlV777131YcffljtucOGDas2rc8//7yqR48eVe3bt6+afvrpq1ZfffWqp59+usHL2b1795LPWW655QrPOf300wv3M890f6tWrap+/PHHivMaP3581WKLLVZtXUaPHl3yuW+99Vbh/7vttlvhNSxvqWXnOVn//vtv1RVXXFG12mqrVc0000xV0047bdV8880Xt++nn35a7bmfffZZYTrcWI/999+/ao455ojvC+/RQw89VHJ5St2uu+66wnO//PLLqoMPPrhq0UUXrZpuuumqZphhhrg9L7zwwqq///672nKMGTOm6vDDDy88l3nPOeecVWussUbVEUccUfXbb79V3L6lttXdd99d1bVr1zi92WabrapXr15VP/300wSv++STT6p69+5dtdBCC8X3kuVceumlq0488cS4XFnF251ts8oqq1S1bt26qkuXLhWXL7svc2Pbl1P8vmSxjSvtt/fcc0/VJptsUjX77LPH936WWWap6tatW9XAgQPLbqsbbrihaplllonrv8UWW9Rr25Tz/PPPV1sX5s3noZRRo0ZVff311422P3/zzTdxfrz/zZo1q3rttdeqfvjhh6p99923asUVV4z7OevFPsI6Mk3Wudh3331Xteeee8ZtyXvNdn/22WfLfj7repyTJJVmOCVJkiZKOEXjs1OnTmXDDRp+jz76aMkGPQ3Tueaaa4LX0OgbPnx4g5azVCOfxjcN2vSc7Dz++eefqhYtWhQeu/feeyvO67nnnqu2zIMGDarVMtY1nPr999+r1lprrbLbl234wgsvlG3Ml3pv2L4jR46sUzjF+jKvcs9jGf/888/CchBCVZou+01dttXiiy9ecjoESGyjhPeU4KDcfAkTvvrqq5LbfcEFF6xq3rx5tWnnGU79999/VbvvvnvZdcmGTtltVfyep+fVdduUQ7iVXjPjjDPG0Ka2Gnt/Jpx67733Ku5rM888c7WA6tdff61aYoklJngeoVb2/uzns67HOUlSaQ6ILkmSJor9998/fPTRR4WxkugCyPhKDDYOBkPeaaedSg40zsDbjO3EoMm33XZbWGSRReL9f//9d+jVq9cEY9k01GeffVZtmnRRTFq0aBFmmWWWwt90S6rklVdeqfb3+uuvHyYGBihnDCx07Ngxdq985JFHQu/evQvbsEePHrErVSljxowJAwYMiN0d55577sL2TeN0HX/88eGpp56q9hqey33cNt544/DXX3+FHXbYoTBQ+jbbbBO7a9H9c+mll473sYxnnHFG/P8PP/wQB6rHvPPOG2699dbYxYsulYxTxODzDCBeF++9917sNjZ06NBw+umnh2mnnTbe/8Ybb8Rxj0BX1J49e8ZubFhxxRXjmGR040zrzj7AvlXKp59+GhZbbLE4TtLDDz8cDjzwwJAn3reBAwcW/t52223jNr/33ntjN1S6o5bC53HVVVeNnynepx133LHB26bcvt+tW7cw44wzVtuGTz/9dLXbm2++2Wj78xdffBEvXMD7c9VVV4VZZ501zDzzzPE+1vehhx6K3W3vu+++sPPOOxc+AxdccEFhGnTlfffdd+P/6RLIxQzuv//+sOmmmxbub8zjnCQpo0xoJUmSVO/KKbpUZStN7rzzzsJj33//feymlx4bPHhwyWqTt99+u/Cal19+udpjr776aqNWTj311FPVpl/chWjeeectPHbaaadVnBddArPTovKqsSunqJyh+1K6n+5zrEO60U0uPZa66hVXmqTtjrPPPrtw/9Zbb11tuSpVAN13332Fx1ieESNGFJbh0ksvLTzG8uCPP/6ommaaaeJ9nTt3rnrllVfifXWV3VZ058s64IADCo/RLQ1DhgypVh1GF7Dk/vvvLzxG9dy33347wXan+qVc18w8KqdWWGGFwv1bbbVVrbfV3HPPPcH2rs+2KWfhhRcuPH+nnXaq9lifPn0mqCpaaaWVGm1/vuSSS0ouE+tA10e69WUrINON7qfJUkstVbj/0EMPLdxP11S2XfHnsz7HOUlSaQ6ILkmSGh2VBP/991/h71RFACoaFl100fD666/Hv99///0JXk/Fw5JLLln4m4HEGaT8jz/+KEx/2WWXbbTlnWGGGar9TUVQub9rGkC6+Gp2P/74Y6NfZe/777+Pt+Swww4r+1yujLbBBhtMcP8666xT+H+2Mqz46oKVZKtJWJ411lij5PNGjRoVtwPz2W233WJ1CYPC8742b948Dvi+0korhT322KPkslaS3bfS35dddln8f6poye5jCy20UBygvtTryeI++OCDOJh+FtVGeVwpsTbbfeutt67166h2m2666ard19BtU27f5/2elPszVXvF2M+oqquE6qnk448/Lvx/lVVWKfyfajwqyu6+++5GPc5Jkv4/u/VJkqSpHt2Ist3JRo8eXe3KX9mGNg34Sghcsh577LFct2/qrlWsffv21bouJo3dZbJ4OehyRTc+upTRjY/uUyNHjoxdrzbccMMwZMiQMLnJBjaNrbgbY7bbWjawmdzXo3jff+6556p1ZSMwZN86+eSTJ8r+XGrd6JaXsG/R7ZEuqRdddFHh/my4JEnKj+GUJElqdFw2noqY5Jlnnin8n6CHCoyEsXxKVTMwllDy6quvFqqmsPDCCzfq8lLxka3Eyo61xLKPHz8+/r9Vq1axiqYSKiwWX3zxwt8nnnhi+O6770o+95133qnX8jKmEJUZCePs/L8L3VS70ZBvaBiQDU+KG/LZ9aT6iSCv3HLMP//88XnsF4zBc8stt8TqKQKM8847rzAd7q+L7L5V/HfaT7L7GGOGZcPH7PNZV6pdKm2DxkaVYNZXX31V+D/jHZWyxBJLFP5fXM1TKWAstR4N3TZZVMUlY8eODUcccUSYVPtzqXVjHKqEfWyzzTaL1U3lAq5s8Pz8889XCwxfeumlRj/OSZL+P7v1SZKkidLg3mKLLQoN5z59+sTGKtU6DECcgiYapXQ1KmW77bYrNERPOumkag3C2nTpoxtN6kqT7VLDoNwMWJwCleWWWy7+/+CDDy40rs8666zYBY3lO/bYYwuv3WWXXapVHJVCY7V///5xIHTCGgaTZnkPOeSQ+C8BD6HUTTfdFOaZZ57CstQFDXG6wKVQZ9dddw3HHHNMrESi4U2jnMY14ca4ceNCQ7Ad2GZgsHQGh2YdCeHWW2+9OLD5l19+GedJd6t99tkndv2iKx9hB4Na854xwHUKjHjPqbKZa665YvCXBkkHA3TXxYsvvhgH66Z722uvvRauvPLKwmPbb799/Jf3gnl98803cdD3rbbaKg7AzrbKvr8bbbRRxW5r9XXOOefEAf6LMQh427ZtY5fBb7/9Nt7HYN2Ed2y37HbJ2nvvvcPLL78c/8/g5VShMTA93c8YlJyAi0HTa6Mxtw1d4Xj/07zZXwiZd99997DAAgvEIDIb+kzs/XnBBRcshNwMlk8XP7ZPGqC/GAPLp8D4f//7X7wwAt2LGXw+Gxo25nFOkvT/lBmLSpIkqd4Dotf2EuuPPPJIyUGk27dvH6dX/Jppp5226vHHH6/zspW7pQHGEwZxLvfcLl26VI0ZM6bWewUDMbMelea/xRZb1GtAdPz+++9Va665Zo3r2JCBt9GjR4+S0/3yyy/j488++2zVTDPNVOvt3KpVq4rPzQ4qXU52Wy2zzDJxsO7i6TDg+m+//VZ4zfDhw6vatGlTdr4dO3YsrFOl7V6fAdHL3dL+dMYZZ5R8PDtAd/Z9GT9+fNUuu+zSoP0qq67bphIuAFBq8PNSt9VXX32i7M/JFVdcUXIa2flkj1u//PJL1WKLLTbB8xnEf6GFFiq5Het6nJMklWa3PkmSNFFQdUB1R9++fcMyyywTWrduHccXooKCCgaqXKi8KYVL0D/77LOxioQqBAZxpjsO4zetvfbaE+0dGzRoUBxEmQoQBj5nvnShooLr6aefnmCw80o22WSTOGAyVVirr7567LZEZQvVJ1QNHXfccdXGxKkrBohnezCG05prrhm3E2NHUYXD9A899NAwfPjw0FAXX3xxrMph+qW6TrGt6J7HINZUmfA+s2yM48X7y/g+p556auH5bI/NN9887gds42mmmSZWljAm0NChQ+s0wDeoXHnggQfigOq8X2xnqneGDRsWlyXp3r17HJx63333jRU17IssZ+fOncMJJ5wQu45SyZaHo446KlYr8ZlhuZZeeum4Lx5++OEln0/lGo/fcccdsSKHfYr3nveoW7duYcstt6zT/Btz27AcjC/Fa3r37h0/P3yeeZ+pHuvSpUuskqL7Jt33Jub+zPpcfvnlsUsd+wYVfP369atWiZnF/vjkk0/GSi/mzzKxfz/00EMTDLzfGMc5SdL/14yEKvO3JElSLmh4rrXWWvH/jE/EINlSKYQH119/ffw/wSHd4yRJUtNl5ZQkSZIkSZJyYzglSZIkSZKk3BhOSZIkSZIkKTeOOSVJkiRJkqTcWDklSZIkSZKk3BhOSZIkSZIkKTeGU9JUoqqqKowbNy7+K0mSJEnS5MJwSppK/PLLL6Fdu3bxX0mSJEmSJheGU5IkSZIkScqN4ZQkSZIkSZJyYzglSZIkSZKk3BhOSZIkSZIkKTeGU5IkSZIkScqN4ZQkSZIkSZJyYzglSZIkSZKk3BhOSZIkSZIkKTeGU5IkSZIkScqN4ZQkSZIkSZJyYzglSZIkSZKk3BhOSZIkSZIkKTeGU5IkSZIkScqN4ZQkSZIkSZJyYzglSZIkSZKk3BhOSZIkSZIkKTeGU5IkSZIkScqN4ZQkSZIkSZJyYzglSZIkSZKk3BhOSZIkSZIkKTeGU5IkSZIkScqN4ZQkSZIkSZJy08JtL01dOvUeHJq3bJ33YkiSJEnSZGHUwJ55L8JUz8opSZIkSZIk5cZwSpIkSZIkSbkxnJIkSZIkSVJuDKckSZIkSZKUG8MpSZIkSZIk5cZwSpIkSZIkSbkxnJIkSZIkSVJuDKckSZIkSZLqaffdd3fbTW3hFG/6lltumfdiTJYGDhwYZppppjClGj58eGjWrFn4+eefw9RmSn9vJUmSJGlysuaaa4ZWrVqFNm3ahPbt24fu3buHl19+uUHT7NWrV1h00UVD8+bNQ79+/Wp8/i233BIWX3zxuAxdu3YNL730UrXHaRvvvffeYdZZZw1t27YNK6ywQvj9998Lj99zzz2hU6dOoXXr1mG11VYL77//ftl5vf3222GDDTaI0yrV7v71119D7969w5xzzhnbpnvssUe1eQ0ePDh069YtzmuZZZaZPMKp0aNHhwMPPDAsuOCC8c2cd955w2abbRYef/zxMDloygEXO+c000wT+vTpEyY3I0eOjDtxus0yyyxh/fXXD6+99lqY0oOjtM4cZPiw7rDDDuGLL77Ie9EkSZIkSfV0zjnnxFCGjGOllVYKW2+9dbXHBw0aFMMj2ukdOnSIAdaYMWPKTq9Lly6hf//+YcUVV6xx3s8880wMg2hvjh07NoZQG2+8cfw//vvvv7DpppuGaaedNnz44YcxTBowYED8Gx988EHYaaedwkUXXRR++umnsPbaa4ctttgi/PvvvyXnx+u23377OL9SDj/88PDpp5+Gd999N7b9v/nmm3DIIYcUHifA4+/jjz8+1Eejh1Ms5PLLLx+eeOKJcN5554W33norPPTQQ2GttdZqUKAyfvz4uPGndtdcc0046qij4s7/559/hsnRY489FkaNGhUefvjh+EHeaKONpvhqJ1Jq1vnrr78Od955ZzwQbLfddnkvliRJkiSpgVq2bBl222238OWXX4bvv/8+3kfbb8899wwXXnhh6NGjR/j888/DCSecEFq0aFF2OmQi66yzTphuuulqnOeQIUNimEQoRoHKvvvuGyuo7r777vj4gw8+GAsiLr300hgMUSix7LLLFsKpG2+8MeYwBFjM78QTTwzfffddeOqpp0rOj4quvfbaKyy11FIlH2e+xxxzTJh55plj5dRx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r1lggQVCv379QlMwcODAMNNMMzVofaek7SFJkiRJqp8111wztGrVKrRp0ya0b98+dO/ePbz88ssN2py9evUKiy66aGjevHmt2pVDhgwJSy+9dGjbtm3o2LFjuOiii6o9/tdff4UjjjgizDnnnHE5O3fuHEaOHFl4/Oeffw577713mHXWWeM0VlhhhfD777+Xnd9XX30Vtttuu9iu5rbBBhtUa29PM800cT7pdu6551Z7/ZVXXhnmm2++MMMMM4RNNtkkjBo1Kkwpmk/JyWqzZs0muH388ccTbZ7stI8//nidXvPSSy/FD1Derr/++tC1a9fQunXrMOOMM8YDw/3339/o6zs5bA8OAHzomVd9sB/dc889jb5ckiRJkjQ1Oeecc8Kvv/4aRo8eHVZaaaWw9dZbV3t80KBBYfHFFw+33HJL6NChQ2ynjhkzpuz0unTpEvr37x9WXHHFGuf93Xffhe233z4cffTRYezYsbGN17dv3/Dwww8XnrPHHnuETz75JLzyyivhl19+CbfffnuhYOO///4Lm266aZh22mnDhx9+GIOqAQMGxL9L+e2338Jaa60Vl/HLL78MP/zwQzj99NOrPadz585xe6TbUUcdVXjsiSeeiMvKMrDss88+e9hpp53ClGKKDaew4YYbxiQxeyMNnVhINmeZZZY6vWa22WaLgVCeCJn23XffsMMOO4Q333wzvPjii2G11VYLW2yxRbjssssadX0buj3++eefBk3/iy++CM8++2w44IADwrXXXtugaUmSJEmSGq5ly5Zht912i6HN999/H+/7+uuvw5577hkuvPDC0KNHj/D555+HE044IbRo0aLsdPr06RPWWWedMN1009U4T6qYqqqqYsBDAQKhEQUbb731Vnz8nXfeiZVVtBvnmmuu+JzFFlusEE49+OCDsX156aWXxsovqrWWXXbZsuEUlVFUWLEOFISwHsyvtq677rqw8847xxCPyqmzzjorPPnkk+HTTz8NU4IpOpyiRHCOOeaodqNiBuxkyy23XNxpF1xwwZiQ/vvvv4XXsuNRMkcSSlhCWvvcc8/FyivKD9kZunXrFlPUct3cqN7acsstw/nnnx/LAAly+LBkA5bibmzM9+qrrw5bbbVVnG+nTp3CvffeW2292AFJglk/pnvMMcdUW/Y77rgjJq7TTz99nOe6664bU9pSnn/++XDBBReE8847L4ZUCy+8cFzXM844IxxyyCHhsMMOiweIUrLr+8gjj8RtSVqcdfDBB4e111678PfTTz8dVl999bhs8847bzjooIOqLVup7XH55ZeHzTffPG5zlmv8+PFhr732ikEj06Fs8+KLLw61/UDznu63334xff/jjz+qPc57yzKRUHOAYZ9hPbPLB94fli39nd7rLLYf06vttLNloYR0lIWy7d54443C4/yftJ2DGY8vv/zyDS59lSRJkqQ80S675pprYngz88wzx/uoLKLNteqqq8a/afutt956sS3UGGjLUolFLyLamK+++mpsb62//vqFdjftPcIk2me0zbPd7Hic9vMuu+wS291LLrlknFY5PH+eeeYJG220UWwP0pYbOnRoted88MEHsUKMtu7+++9frX1NIUk2b6ByijZlCtOauik6nCrnqaeeCrvuumsMTt59990YQpFiEnxknXbaafF5r7/+ekxIe/bsGSuMjj322BgIkLJSgVPJsGHDYoDFv+yozIdbJQRllBey82288cYxyf3pp58K6TH3kbDywSG44UOcygGpDiNVJmF+7733wvDhw2NpJMtaCgENFVCsV7HDDz88Bml33nlnjduUdJoEOftcPuC33XZbodSQ7UA12zbbbBPXjccIq2rahgQ4hEF86Fgvyif5UFPOyPt30kknheOOOy4MHjy44nTYBilt5v3kQEKQV4z3iSDshRdeiAefU089NTz66KPxsdQVkOmwrevaNbDStEH/Y0o0SeEpHSVAZdum959tybozXx4nmCyXzNM/ety4cdVukiRJkjS5oG1NO5I20s033xzuuuuuQmUUBRcUFvAvwQ5tKQKrxkKlE0UGhx56aCz8YLwoCjYYgwq0wWhv0l6mYINufxRF3HDDDYXHaecTntE2vOqqq2LbdsSIESXnx/NZP9re3377bTjxxBPDtttuWxh6aI011ohtXro40oWProJUkyV088uOAQ3+prvhlGCKDqcYMyk7mBgN/xT+0KjnjaZqivSVIIqQKov+pYREiyyySOzbycBnhAOMWUR1EeEW4U8lpL50jSMM4YPFoGU1jdPEB4SAifDkzDPPjDshXe1A/1kqjtI0qdZhfah+IrThQ0EVFYEUKS8fZBJX1r8UdviFFloollEWo3SR6hyeUxMq0nbcccd4QElYT5JewihQdsj2o6KI1JnK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5Mj42KhRo8Lmm28e5pprrtCsWbPw+uuvT/D6M844I8w///yhbdu2Ydlllw2PPPJI2XkNHz48Tof5pNsBBxxQeLx3797VHmvdunV8/quvvhoff/vtt8MGG2wQZp111nj/zz//XM+tJE3CcIpkmR22+Pbxxx+Hqd0ff/wRD358qDkYTS1+//33cOyxx4aFFlooTDfddGG22WaLXwBDhgwJTQ1fGOzPHTp0CL/88ku1x5ZZZplwyimn5LZskiRJkmrnnHPOCb/++msYPXp0WGmllcLWW29d7fFBgwaFxRdfPNxyyy3xtz/tlzFjxpSdXpcuXUL//v3DiiuuWKv577HHHuGTTz4Jr7zySmxX3H777YWiAAKuDTfcMNxzzz0lX8v9559/frj//vvD2LFjw2GHHRa22mqr8NNPP5WdX7t27eL6pttll11WeOyKK66o9thpp50WFllkkbDccsvFx6eddtqw/fbbx8IFqUlVTvFBIu3N3jp27Fivmf/zzz9hSnHnnXeGJZdcMiy22GJlDzRTIpL4u+66K1x66aXh/fffDw899FDYdtttw48//jhR5/v3339PtGnzBcIXgiRJkqSmq2XLlmG33XYLX375Zfj+++/jfV9//XXYc889w4UXXhh69OgRPv/883DCCSeEFi1alJ1Onz59wjrrrBNPxtfknXfeiSfqr7322kJ1FG3EFE7NPvvsYf/99y8bdH366aeha9eusdqK1+6yyy6x3cz9jeGaa66J659QEbbXXnuFpZZaqlGmL02ycIoSyTnmmKPabZpppomP8SEkgeVDu+CCC4a+ffuGf//9t/BaPlyXX355LGOcYYYZYrki1ShUpdxwww1hgQUWiKnvjjvuWK1yhcBjtdVWix/oWWaZJWy66aYxiS6ueCEkWWuttWKpIun2c889V23ZSYPnm2+++Djpc3GAwjS32GKLeMCg5JGDwmOPPVbrD/nOO+8cb/y/eL6lKs6ylThXX311TO/Zdhy8SOaTbt26haOPPrraNDm4knKPGDGiWuno3HPPHbctZwgo8azL+oP3hyooDuQcqHhfKrn33nvDcccdFzbeeOP4/i2//PLhwAMPrHbA4yzErrvuGmaeeeY474022ih89NFHhcdZDr4YWHYe50DMWYzi8lzKUw855JBYnUbpaSpDZXq8X7xvHLx/+OGHwuvuuOOOOL3pp58+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kpQbwylJkiRJkiTlxnBKkiRJkiRJuTGckiRJkiRJUm4MpyRJkiRJkpQbwylJkiRJ0mRj9913z3sRJE1iU1w41axZs3DPPffkvRiSJEmSpP9nzTXXDK1atQpt2rQJ7du3D927dw8vv/xyg7ZPr169wqKLLhqaN28e+vXrV+PzaSu2bt06LgO3Ll261OnxIUOGhKWXXjq0bds2dOzYMVx00UW1Ws5HHnkkTvuQQw4p+fhVV10VHy9eB9q1nTp1isu02mqrhffff79W85OaouZNJTnnw8pt2mmnDbPPPntYb731wrXXXhv++++/as8dNWpU2GijjcLk4OOPPw577LFHmGeeeeKBmANYjx49GnwQTk455ZSwzDLLNGgaw4cPL2zbcjeeMyV57rnnwjTTTBM22WST3La7JEmSNLU555xzwq+//hpGjx4dVlpppbD11ltXe3zQoEFh8cUXD7fcckvo0KFDDLDGjBlTdnqER/379w8rrrhirZfh2WefjcvA7Y033qj14999913Yfvvtw9FHHx3Gjh0bg6O+ffuGhx9+uOL8fvvtt3DQQQeFbt26lXz8m2++Ceedd17o3Llztfs/+OCDsNNOO8UA7Keffgprr7122GKLLcK///5b63WVmpImEU5hww03jMHTyJEjw4MPPhjWWmutcPDBB4dNN9202gd0jjnmiEFQ3gigll9++fDhhx+GK6+8Mrz77rvh7rvvDosttlg4/PDDw+SCgyTbNd044KZtnW7lDqQTS1VV1UQ96F5zzTXhwAMPDCNGjIhfBpIkSZImnZYtW4bddtstfPnll+H777+P93399ddhzz33DBdeeGE8of/555+HE044IbRo0aLsdPr06RPWWWedMN100030Zf7qq69iO4XAiBP4BGNdu3YNb731VsXXHX/88aFnz56xAqrcOpx44omxmizrxhtvjG1e2rusH88hIHvqqacadb2kyUWTCacInAie5p577rDccsuF4447LpZVElQNHDiwbLc+DngELjPNNFP8wJM2E3AlhCAk2Tw+yyyzxCScA+WWW25ZeM5ff/0Vn0N6z4GBksqXXnqp7LJy0KLaiwMQBw8qdBZaaKFYbXPyySfH5U44mJGCTz/99HH+lKaS0idULXEmYIYZZojLuOqqq8YDNetMUk+anyqc0nbggE7yzmvmnXfesP/++1ebZvEXA9s13ViOtK25vf7663H50vbh4PjJJ58UXk9wxTbL4guGCjfCH9xwww1hhRVWCDPOOGOcJgdnDqzZdWT5eS8J9Jj/008/HavizjrrrFhxxnLxBXDHHXcUXsdZFL4cZptttvg42/u6664LlbAdbrvttrDffvvF9yW772SX5fHHH4/LTAkt68iZC5Tb7uxT/J/tlfz888/VKs9qmnbC/sE+zr624IILxvmlsI59i8qt+eabL26nueaaK+6bkiRJUlPxxx9/xBPGs846a5h55pnjfT/88EP8rUx7B/y+p7cMbYjGtPHGG8f2A6HW888/X+vHactRyXX99deH8ePHh1dffTW2CdZff/2y83rhhRfCY489Fo455piSj9O2GTduXNh1110neOzNN9+s1luD9tUSSywR75emRE0mnCqF0ITA4q677ir5+D///BM22GCDeEAjJHrmmWdi32Eqg/7+++9CaelNN90UQw0e5+BQPGbVUUcdFe688854IOIgtPDCC8fpUl5ZCgHFO++8Eyuk6P9cjKAnlXgyHQ7IhF233357PHgdcMAB8XECCUIyDoIchOiORnjFQXuHHXaI019yySULFU7cB+Z5ySWXxGVgmZ944om4DvXBMh522GGxEoxQhWlvtdVWhe6UhEO33nprDE0Swh9Ck9VXX73wPpx22mnx4M22JcgpNcghB+2zzz47vPfee7EvN8EUpb1XXHFFXJdDDz007LzzzuHJJ5+Mz+fsARVphFq85vLLL49fcJUMHjw4Vq/RN51p0TU0u+zZMxwXXHBBXG/O1nAWB5W2e22VmzbYT/lyoiqQdaPqjvDrjDPOiI+zH1Lay/0fffRR3J7FJcDZUJX9OXuTJEmS8nLsscfGthAn0W+++ebYjkuVUfym5UQ4//J7n3YMgVVjol302WefxfYIIRTB0hdffFGrx2kH0YahTcJJYk42H3HEEbHdUgptoH322Sd2O6QgoBgn2o888sjY1il3Uj21GxP+/uWXXxq4FaTJU5MOp0DQkK2EyiIkIUS5+uqr40GO/suEUBxgUjXLpZdeGg+SBC5M67LLLqt2ECCcIfSgHzBjWZFWDxgwICb5pP2lEBqkZauEA/Kff/4ZA5illloqhm3Mn0qjb7/9NoYJ9GfmIE3lFctPVRdVM8yfoI2DebbqCQy0RwnoAgssEKd5+umnx1CmPrbZZpvYF5xA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DnvuuWe48MILQ48ePeLJ8hNOOCG0aNGi7HT69OkT1llnnfg7v7aOP/742F7o1KlTxefRfmA5pp9++vj3gw8+GL744otw6aWXxsovqrWWXXbZsuFUqemxflnjx4+PlViXXXbZBL/Br7vuutgmI8Sjcuqss84KTz75ZPj0009rva6S6sdwqkQYMdNMM1W7j1JPKpzKdevLVkGlG12yKiF0mGOOOWJav/LKK4cDDjhggnJTDoSckaAUl+cdc8wx4d9//61WgcXrKI2lzHWDDTYoVONw4OcLY6211grXX399XCbONCRPP/10WH311eOBf955543BEmc0Es6GpGlwxmDbbbctuy633XZbuPXWW+O/J554YlwfSmH5lzM1HOQTzn6ceuqpYZ555onrxXZ86KGHCo+PHDkyLuvgwYMLy9e1a9d4poRKIsp4CQc5m5K+VJOrr746nvVhmRdbbLG4Dtngjm3FduTx+eefP37Z1BS6sey77LJL/DLlyy0rLSvrzRkmpnvTTTeFH3/8MX6pzj333PF97ty5czwTVVOXPbYF+1a55/DFvMUWW8T1pzqN0Ozbb7+tuA6SJEkS/vjjj/h7lnbDzDPPHO/74Ycf4u/ZVVddNf7Nb+/11lsvzDjjjI220TjB+9hjj8W2TE09Fh5++OEYHGXbQwsvvHD8PU5xAD0zaNvUxnPPPRc++uijCcbSuuiii8LSSy8df78Xo0dDtp1HO4g221tvvVWreUqqP8OpRkAFVLrRhY0D6BprrFHr1//0008xjCGhTziLQRUSwQxlp5dffnn8MimuQuLgTOL/zDPPxDLWzz77LAZJdFvkdfvuu288U5H1ySefhA033DBss8028QBMuEJYRXgD+qETVhEiffDBBzE8qrQ+BC/0O6cKqJRssHfxxReHCy64IJx//vlx3gRqvI4vjqyTTz45nrUhsOPMDeHQUUcdFV//1FNPxe180kknFZ5PKMTfZ5xxRnjvvfdi/3WCsvTldckll8TQju3MOvH8mgJEKproz77uuuvGMygEcNkAL+GLlu6LzJf1+fPPP8Pyyy8fHnjggfD222/Hrnl8ob744ouhvgj1CKbYV/iSfvTRR+MZnB122KHe05QkSdKU79hjj40n36kEuvnmm+N4TqkyipOodJvjX35j8tuZwKqx0KuAHiOcNC7VUyCLk8KERvyOTvjty29y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5QEAAAAAAID/GJVTAAAAAAAACAzJKQAAAAAAAASG5BSQZp5++mn37rvvBr0YSAGxSh/EKr0Qr/RBrNIHsUovxCt9EKv0QayCRXIKCFhOTo4rUaKE3cqUKePq1avnevTo4f78889dnrdayvXu3dvVqFHDlS9f3rVo0cJ98803+b5vxIgRrm7dum633XZzxx9/vPv0009jXtdrWt6JEyfmem/Dhg3tNX25Z5qwxWrQoEHuuOOOc5UqVXJ7772369Chg1uxYkXMNMQqHLHq27dv5P+OfzvkkEOIVUi3rX/++cfdc889thx6T/369V3//v1tXr7TTjvNlnfw4MG53t+mTRt7TXHPNMUZq5dfftm1bNnSVa9e3ea/YMGClN43efJk2560zzriiCPc66+/HvM6sQpHrMaMGeOaNm3q9thjD7tpW4w/vsjWWIVx29JxXPx+S9tYtGyNV9hiJQ8//LBr0KCB7bNq1arlunfvHrM8/jJfc801ud57/fXX22uaJtMUV6z++usv17NnT9vnVKhQwe23337u8ssvd2vXrs33vfzOyoMaogMITufOnb0zzzzTW7dunbdq1Spv6tSpXuXKlb0ePXrETDd79mzvpJNOsteqVq3qNWrUyBs5cmSe8x48eLBXpUoVb9q0ad7ChQu9du3aefXq1fN27NiR9D0TJ070ypYt640dO9ZbsmSJ17VrV/u8DRs2RKapU6eOV6tWLa9ly5Yx7503b55XrVo1r0KFCt64ceO8TBO2WLVq1crW8+LFi70FCxZ4rVu39mrXru1t3749Mg2xCkes+vTp4zVs2ND+7/i3TZs2xUyTrbEK47Y1cOBAr3r16t706dO9lStXepMnT/YqVqzoDR8+PDJNs2bNLF4NGjSIee+aNWu8cuXKeTVq1LC4Z5rijNX48eO9e++91xszZoyygN78+fPzXZ65c+d6pUqV8u6//35v6dKlXq9evbwyZcp4ixYtikxDrMIRq06dOnkjRoywaZctW+bl5OTYtqltJttjFcZtS/sbfUb0fmv9+vUx02RrvMIWqwkTJtj61r32WbNmzbJ1371795hlVqy0zf3xxx+R57Uv1LLp+FHTZJriitXWrVu9Fi1aeJMmTfKWL19ux2pNmjTxGjdunOfy8Dsrb6XzSlwB+O8uPbrvvvvav3W2Q2cT33rrLTdkyBB7buvWra59+/bu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5caNGxeTnFq/fr276aab3Ntvv+1++eUXq9Y6+OCDXf/+/S2JVBzi1++uqlatmt2KU6lSpVxOTo4l+UhOAQCKGsP6AAAAApRs+JqqavRaNFUwnXzyyW733Xe34VsahjZ//nx77d1337VhXZqmY8eOrnLlypGhbj/++KM9pyoiVda0atXKLVq0aJeWO795qopH06iqyR9ypuFsouqbU045xRIq/t/x6aefFmo5NC8tR360jEpirVq1Kub5rl27ujlz5rhHH33UklmTJ0927du3d5s2bcpzfv76njVrlrvgggsshrVr13bPP/+8va4kjh7rb7zqqqvc//73v6TD+vKi9VenTh1bzx06dMi1XKnGVp+pKqvddtvN1axZ0919990xQ/S2bt1q60KvaRol8uIrzPT/acGCBW7hwoX5LjcAAAVB5RQAAEAamDRpkrv44ostcaIESNmyZd3cuXPdTz/95Bo1ahSZrlu3bu7SSy91U6dOtWqX3377zZI/JUuWdKNGjbLEw8CBA92pp55q/YqUhCioVOapz9dwPiWhbr31Vntf/fr1Iz2WNMROj3fu3OleeOGFyHtVtZSqb7/91ualhF1+/v33X7dmzRp31FFHxTz/3nvvuZtvvtl16tTJPfHEE+6ss86yW6quvfZaqyhSYmfMmDHusssus+TN4sWLbd18//337pZbbnEHHHCAu+uuu1xBvPrqq+6bb76xBJUSWd27d3c33nijmzhxor2eamwffPBB16NHD3v/sGHD3LJlyyLJqcGDB9s0WsY33njDHiuxqGGCehxNPaeUTHzrrbdyrUcAAHYFySkAAICQ8zzP3Xbbba5ly5aW9PEl6uXUrl07N2TIkMhjVfCoukZ9iZRckGbNmllVj3pCKVlRUBoal988lTArV66c22effdwJJ5wQ8/7evXvHJI3OOOMMq5xSdc99992X8nJ89tlndq+KoESUfPn7778tsaN1snnzZnfnnXfGTKNm4p988klMZVNBqJrI/3uaNGniXn75ZUu2fffdd9bfyq+yUkVWQZNTirsSVFqPokSc1o/WmRJSqcRBCaw+ffpYcspft1rfSm4qIaVm8tWrV7f1rwRd586dI5+fqDeX1rXWFwAARYlhfQAAACG3YsUKq/q54oor8p02vk+SGoUffvjhkeSFaKiZEhQffvhhoZZnV+epyp1zzjnHEleq7lISR3/j119/XaDlUHWPkjRKriSy77772ryVgFKyRremTZvGTKPknRIz++23n1U7qfJIyZ5U6W/2aWjd3nvvbZVLfmJKVA22evVqV1BKNPmJKTnssMPcX3/95TZu3JhyHD766CO3fft2S6IpUeffWrRoYT3J9DfLMcccY8nBoUOHRp5LRD28tN4BAChKJKcAAABCThU/ogRKfpTwibZly5Zcz/nTqQF4YezKPFXJowowVfxouJkSLKqA0jCxP//8s0DLoemVBFL/pkTU5FyJp5deesk1bNjQGp9ruFs09WjS0Dv1nFIiaMKECVYdNGjQoJSWIf6Ke6pISvRcQf+2ZPMWf16pxMHva6Xkk9aVf1P/LfGTZvr7NSRR1VZHHHGEVV89/vjjueatdaSkFgAARYnkFAAAQIDUJ0jVMNH0WNUuPr8yaO3atfnOLz5Ro0oav9Im2oYNGwp9hbddmee8efOsCkxD0i655BLrSXXssce6bdu2FWo5NBwvWeJHCa/jjjvOnXvuudY/qXTp0q5nz565plMfJQ1pU8Jm6dKlNtxNPZkKm7z7r6QSB/9eww2VBIy/+f21VPWlyjJVRSmBpwTiddddZ8nDaGqcnqxSDQCAwiI5BQAAEKD999/fmoKrR5Fv9uzZMVdSa9CggU2nhE5BKfmjq7dp2JxPFTeqKtJrhZHqPBNVDPlVN34VkD/0TP2UCkrrRVauXJnvtGoOrobgM2fOjFzh0O/rFE8N1vW8/qYwSyUOJ554ol3dUQlBJQHjb4kSTaqceuihhyJDMKMpTv56BwCgqNAQHQAAoJgp0TRlypRcz6uBtipXKlSoYFd7U1WPkgjDhw+3iqroaij1AtLV+s477zy70p2GV6kKSZVBbdu2TfrZXbp0sUSDelENGDAgckU3VRHpKnWFkeo81QtJiTZd3U3VSfXq1bPm6BUrVnTXX3+9u+OOO+xqg2rYXbNmzQIvh9afPvOLL76I6buUjCqiNHxNzdH9K96pcbuSVrpXFZaWtVevXtYnSssbZqnEQUMD+/XrZw3R9X9LV/dTny8NZXzllVdsyKOSV0rIqQ+Yeljp9fHjx1sCMbpH1++//+6WL19u8QIAoChROQUAAFDMVD2khtTxt/fff98qV5Qg0PCsDh06uCeffNISA9GNsOXCCy+0ZIKSObqKmhJVanqtiqq8VKpUya4WpyFu3bp1s6F0ShTps1VNVBipzlNXh9PyKaGmJNprr71m/ZB05Tr9ve3bt7ehZKNHj3YHHnhggZdDST0l9zRkLxUa4nbjjTdaotCvVNO6HDlypDUf//jjj214X/369d306dOt2XqYpRqHW2+91aru5syZY7HQ/70nnnjCYuJXsCk5pf93eq1jx45WjaZ4RSf9Zs2a5cqXLx8ZCggAQFEp4SWqZQYAAADSgBIoSiipz5IqgHaFqoqU7EFiSlwpITZ27FhWEQCgSIX7dBAAAACQBw1p1BA8VZyh+KiSasaMGdYoHgCAokZyCgAAAGlL/bhGjRq1y1VTkpOTUyTLlIk0nFRDATXkEQCAosawPgAAAAAAAASGyikAAAAAAAAEhuQUAAAAAAAAAkNyCgAAAAAAAIEhOQUAAAAAAIDAkJwCAAAAAABAYEhOAQAAAAAAIDAkpwAAAAAAABAYklMAAAAAAABwQfk/XHViprOSTacAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 1200x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "top_clientes = (\n",
    "    df_analitico.groupby(\"full_name\")[\"lucro_total\"]\n",
    "    .sum()\n",
    "    .sort_values(ascending=False)\n",
    "    .head(10)\n",
    "    .sort_values()\n",
    ")\n",
    "\n",
    "fig, ax = plt.subplots(figsize=(12, 6))\n",
    "\n",
    "bars = ax.barh(\n",
    "    top_clientes.index.str[:30],\n",
    "    top_clientes.values / 1e6,\n",
    "    color=COR_NEUTRA, edgecolor=\"none\", height=0.6\n",
    ")\n",
    "ax.set_title(\"Top 10 Clientes por Lucro Gerado\")\n",
    "ax.set_xlabel(\"Lucro Total (R$ milhões)\")\n",
    "ax.xaxis.set_major_formatter(mt.FuncFormatter(fmt_milhoes))\n",
    "for bar, val in zip(bars, top_clientes.values):\n",
    "    ax.text(val / 1e6 + 0.01, bar.get_y() + bar.get_height() / 2,\n",
    "            fmt_brl(val), va=\"center\", fontsize=9)\n",
    "\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a26ccc97-a9dd-42d0-894e-003143bc0e53",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "6b40fc5d-fe35-42f5-98cb-c9efb16acee4",
   "metadata": {},
   "source": [
    "## Projeção e Simulação de Cenários\n",
    "\n",
    "Regressão linear aplicada à receita mensal para projetar 2025,\n",
    "combinada com simulação de impacto cambial na margem."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "6b7f92b4-f7ce-450c-b4fd-2b0954e3acca",
   "metadata": {
    "jupyter": {
     "source_hidden": true
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Crescimento mensal estimado: R$ 757,134\n",
      "R²: 0.383\n",
      "Receita total projetada 2025: R$ 1,534,860,127\n"
     ]
    }
   ],
   "source": [
    "# preparar série mensal\n",
    "df_analitico[\"mes\"] = df_analitico[\"sale_date\"].dt.to_period(\"M\")\n",
    "mensal = df_analitico.groupby(\"mes\").agg(\n",
    "    receita=(\"total\", \"sum\")\n",
    ").reset_index()\n",
    "mensal[\"mes_idx\"]   = range(len(mensal))\n",
    "mensal[\"mes_str\"]   = mensal[\"mes\"].astype(str)\n",
    "mensal[\"receita_mm3\"] = mensal[\"receita\"].rolling(3, min_periods=1).mean()\n",
    "\n",
    "# treinar modelo\n",
    "X      = mensal[[\"mes_idx\"]]\n",
    "modelo = LinearRegression().fit(X, mensal[\"receita_mm3\"])\n",
    "mensal[\"tendencia\"] = modelo.predict(X)\n",
    "r2     = r2_score(mensal[\"receita_mm3\"], mensal[\"tendencia\"])\n",
    "\n",
    "# projetar 2025\n",
    "X_2025    = pd.DataFrame({\"mes_idx\": range(24, 36)})\n",
    "proj_2025 = modelo.predict(X_2025)\n",
    "meses_2025 = [str(p) for p in pd.period_range(\"2025-01\", periods=12, freq=\"M\")]\n",
    "\n",
    "print(f\"Crescimento mensal estimado: R$ {modelo.coef_[0]:,.0f}\")\n",
    "print(f\"R²: {r2:.3f}\")\n",
    "print(f\"Receita total projetada 2025: R$ {proj_2025.sum():,.0f}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "id": "704bc331-f7ac-47da-ad2a-b4033a57444c",
   "metadata": {
    "jupyter": {
     "source_hidden": true
    }
   },
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABjUAAAJOCAYAAAD/KYUYAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjgsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvwVt1zgAAAAlwSFlzAAAPYQAAD2EBqD+naQAA6TZJREFUeJzs3Qd0FOXXx/FLKiX03rt0UIqAoKIgxQKIooKCKMrfjmLDig3FCvbyir1jQbGiKCIKFlCQpvTeewskIe/5PXGW2WQ3pFAS9vs5Z89udmZnZmfLk507994CqampqQYAAAAAAAAAAJDHRR3pDQAAAAAAAAAAAMgKghoAAAAAAAAAACBfIKgBAAAAAAAAAADyBYIaAAAAAAAAAAAgXyCoAQAAAAAAAAAA8gWCGgAAAAAAAAAAIF8gqAEAAAAAAAAAAPIFghoAAAAAAAAAACBfIKgBAAAAAAAAAADyBYIaAAAg4gwYMMAKFCjgLvfcc8+R3pyItWTJksDroAuQ3x3J75Z7773XihYtaieddJJNnjzZXn/9dStbtuxh3QbgSPnyyy/d+71evXruvb9w4UL3OZw9e3aeeFH0feB9N+h7AgAA5A5BDQAAkC2vvfZa0IFo71KoUCGrU6eO+7GeVw4iZNeWLVvcgQfvcrgOcOgSHx9va9euzTDfs88+m2FfKxgQqT7//HO76qqrrHnz5lahQgWLi4uzkiVLugO5r776qqWmpoZ83KxZs6xv375WqVIl9xhd6+9Q79WcrGPIkCFueuXKla1gwYLu9axSpYp1797dPvvssxw910mTJrnltm7d2i1XyyxWrJgdf/zxNnLkSNu7d2/Ixy1dutQGDRpk1atXd48pV66c9ejRw37++eeDtg7Pjh073Ofe//6cOHGiHW4dOnQI+b1UpEgRa9Sokd144422bt06O1olJibaAw88YE888YSdccYZ7n2n7+IrrrjikK1z69at9tRTT1mvXr3smGOOsRIlSrjPStWqVe3CCy+0v/76K+Tj9PnRQef27dtb8eLFrXDhwta4cWO77777bOfOnbleh95/od4L/ou+D/KCo3k8PdwefPBB9z5RcE+3tf/0ndywYcPD8r1DoAIAgMMsFQAAIBteffVVHdHN9FKkSJHUGTNm5Nn9+u+//6b+9NNP7rJ06dLA/YsXLw56HofSsGHDMuy3e++9N2ieffv2pdavXz/DfNrOo0FO9ne9evUyfe9deOGFGR7z5ZdfpsbHx4ecv2DBgqnjx4/P9ToO9Jl44oknsr1/unTpkukyTz755NSkpKSgx0ybNi21ZMmSIeePiopKfe2113K9Dr/LLrssw2N++OGH1MNN23mg16B8+fKp8+fPPyLfLYeaXqO5c+em7t271/29e/fu1FWrVh3SdU6ZMiXT/R0bG+s+e+n1798/7GOOO+641C1btuRqHXr/Hei98Pfff6fmBUfDeJpXLFy4MPDeSUlJSV22bJm7PlzfOxdffHGm8+r7wPtu0PcEAADIHTI1AABArvz000/2/fff2yOPPGLR0dHuPp1t+8wzz+TZPVu3bl13lrAu1apVs7zihRdesKSkpMDf48ePt3nz5h3Rbcqrr5/OSv/mm2/svffes2OPPTYw7e2333bZB57Nmzdb//79bc+ePe5v3R43bpy79s5wv+iii9wZ4Tldh3Tp0sUef/xx++STT+y7775zGTbly5cPTH/sscdy9FyVPXH77bfbF1984ZZ9yimnBKb9+OOP9s477wT+Tk5Odtknes5y+umnuywRZSnIvn377Morr7RFixbleB1+2o8vv/yyy0zJS7p16xb4XtJr6H0vKRPq5ptvztIylIGSn75bYmJirH79+hYbG+v+1mtSsWLFQ77eqKgoO/PMM+2VV16xb7/91kaMGOGyY0TfZddcc03Q/G+99Za98cYb7rayEfQ5+eCDD1wWhvz55592yy235Godfpdccol7L6S/1KpVy/Ki/DKe5vTzcSjpNVXmj/eeUTaPrvMKfR943w36nsiv8uJrDwCIULkMigAAgAiT/sxSvzPOOCNwv84AT2/58uWpgwcPdmfC6wx5nYHavHlzdxa7d4axX2JiYuqTTz6Z2q5du9QSJUq4s3IrVqzo1vPLL78EzTtnzpzUgQMHptasWdOdlV+0aNHUE044wW2vMh78dEalt53KmMjKmd7e2edPP/10ateuXVNr1Kjh1hETE5NatmzZ1M6dO6d+/PHHOcrUKFasWOD2u+++G5jn9NNPzzA9VKZGdvarf73aD5MnT0495ZRTUgsXLuzWc95556WuXbs26DE6A7xv376pVapUca+B5q1evbp7HfT6eJKTk1Ovvfba1Pbt26dWqlQptVChQqlxcXGp1apVc4//888/c52pobOy0599q+2Njo4OLOfhhx8OTHvqqacC9x9zzDGB94KWUbdu3cC0Z555JsfrCEf735s/ISEhNbuUQbJnz56g+3bt2pVarly5wHKvvPLKwLTPPvss6D2leT2dOnUKTLvppptyvA7PunXrXOaDpus9kNNMDb1nXnjhBfee8T7jer8oA2TRokUH5Yxpf2ZA8eLFQz7mlVdeSR05cqTLjNI26PPk+euvv1L79evntkvvZ33uW7Vqlfroo4+676gDfbd4du7c6d43eqyWoWXVqVMn9YYbbnD7M5SxY8e6z5n2tbardOnS7nvNn3HzzTffpPbu3dt9/kuVKuW+k/T6H3/88amPP/54yO/WNWvWuPdBgwYN3OdU3xt6/PXXX5+6cuXKLO1zfe+EyiDQOv3vB//3ib6XvPsfeOCBwP36HvLu1/f3xo0bc7wOf6ZG+tcgksdT7UctR9/fyua64IIL3DL0XR7qs5vVz0d2xt4VK1akDho0yM2r97+2W+OKvp/uvvvuoHn1PXzaaaellilTxr2n9dnVc+3Tp09Qds6CBQtSL7nkEpflo+8tb4zSe1vv5/Tjmeg7b9SoUalt2rRxnxU9RtuhZf/xxx+HJFMj/dgb6j2g5c2aNSu1e/fubrv0PLp16xYyw0yfkTvvvDO1adOm7rXXvmzYsKFbz/bt24Pmze4+Sr9Nv/32m3uN9NrqexoAgLyAoAYAADgkB2F0kMNPZUT0Yzhc0EAH1v0HCPWDXT/Aw82vAyyeTz75xP2gz6xckP/gSm6CGq1bt850Pv92ZfUAh5apA5C6rQCO6CBGgQIF3H06gBQuqJHd/epfrw4s6WBR+sf4D6Bt2LDBHSgNt3wdZPKo5E1m+0YHsaZOnXpIyn3pwJe3nGeffTZwf8+ePQP3DxgwIOgx/vdBr169cryO9LS/dSDce011Oeecc1IPlpYtWwaWe/PNNwfu18Ep7/4OHToEPcb/uuvAZ07XkX6/6kCXPluhPisHouCJ3p/h3i96X//666+5Prh43XXXBabpAH6ox/gDXN5nThRk1AHAcNvYokWL1G3bth0wqLF+/frUxo0bh11O5cqVg4I42qd6v4abv0ePHoF5b7311kw/d/55vYPQ/qBV+ove57kpd/T5558HLW/Hjh3u/s2bNwe+03SZOHFiUPks/3eRAnQ5WUf6oIYCzjoQq4PtCiAp6Hqoy3LlxfFU5bbSB8d1UUDD//0eLqgR7vORnbFXgZbatWuHnVevkWfChAlB75X0l//973+Beb/66qtM3/86AUHvPY/eKwpmhJtf78PXX3/9iAQ1dNKGAhTpt0nBCn+gXf8fKAgT7jnou8YLDOZkH/m3Sd9N+t4MFRgGAOBIyjv5mAAAIF+aPHmya8yq0jsq1SNq5KoyNx6V/jn//PNdI24555xzXKmbDz/80Jo2beru++GHH2z48OGBx6ikiEqReMtT2Rg9RqWABg4c6Boay/r1661fv36ujJCoMe7XX39tb775pmuU7JULUoPnzDz99NM2ZsyYoPv85UqOO+44d9/FF19so0ePds2k9bxVDkWlQbztUQNwlQHKLq+Eipo563lre3QCisqsqIRKKDnZr36LFy92pYZUomjYsGGB+/U6/vPPP4HHb9q0yd3WvHremq5SMJdddpkrXeQvgXPXXXe5/f3VV1+5/fPll1/aDTfc4Kar6bSaAR9sKteyYcMGd1slW1R2yeMvtaSm337+vxcuXJjjdXjGjh3rGsaq9I/KVf3222/ufaHyVv/3f/9nB8O///4b1BxZDaEP9nPNbB2i117PVc3TvUbHOaHPit5fUrNmTfcZVck1r7m13td9+vTJ0efJK02kz65KHnm8z3F68+fPd89T5bf03E477TRbs2aN+67xSsKprJVKbj333HOBMjfTpk2zoUOHHnBbrr766kBzar033n33XfcZ0WdWVq5c6b5bPHq/aN96zj33XPe51mf1zjvvtLJlywamqRmymmlruydMmODeq/oMqlGyfPrpp/b7778H5tf70WuarjI42hZ993kNlfU+VxNulSvLiffffz9wu2PHjoFSUfq+SWs/k/E9qe+O0qVLZ/k9Gm4d6Wl82L59u/uuXLBggfte1f7X6x1J4+ngwYNt27Zt7rbKkqlRu+bXfvO+3zMT6vOR3bF3xowZgddV26llafzUtmj7vPerfPzxx4H3ylVXXeVK+um9r7H27LPPtmLFigXm1bpUkkzPR98f2n9adteuXd30JUuWBH3/aoyaOnWqu52QkGBPPvmkG9d69uzp7tP3zaBBg2z58uV2uK1evdrq1atnH330kY0aNSpQTm7OnDluX/k/wytWrAiMy3q++m46+eST3X36rrn++utzvI/89N1UqlQpN12PPRRjOAAAOXJEQyoAACDfOVBj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qIEjTgEA7xIdHW3x8fGBv7t163ZI1z127FhLTk627777zq688krXg+Rg2LFjhzVp0iTXyznxxBNdo/e85IcffnCNsk8//XT398SJE12wSK9X0aJFrXr16nbbbbfZPnU1M7OVK1faueeeaz169LDOnTvbxo0bc9Qzpm/fvu7s5PLly9v999+f6fxaX8WKFd38Clg98MADQdMnT55sbdq0cX1oKleuHLS9eg79+/e34cOHZ3s7AeBwlN8YM2YM5acAABGF8Q8AAPhRfgpHnAIAHp192rNnT5c9cThoXbqIAhsI/uEQGxubYZc8++yzdskllwTdp+CAMmFk7ty5duqpp1rdunXt0ksvtUqVKtmHH37opl111VX2yy+/2FlnnZWtXX3ttdfapk2bbNmyZbZu3Trr1KmTC54o+BDKsGHD7JhjjnEBMj1GmSU1atSwiy66yFJSUlyA5aabbrKff/7Zli9fbqeccoqb/r///c89/uKLL7Zjjz3WBTYKFy7M2wJAnqEgsjL4KD8FAIgkjH8AAMCPTI0ItXPnzrCX9NkKmc27e/fusPMeDNOnT3cHnEuVKmV16tSx//u//wtMu+eee9zB8WuuucZKlChh1apVs/fffz8wfc+ePS77Qo/V2fregXVPamqqPfXUU1a/fn33eAVUdEDeo4PcjzzyiDujX2fvn3zyye4AuGfNmjXuILkyAvT4k046KbA/9E/3X3/95W7/+eef1r59e7cdZcuWtT59+mQ5W0FZEFq2R9uorIIuXbq4bWrevHlQmSsFiLQ/tC/KlSvnDvpv3bo1MF3bqyCDMhhatGjhsi48r732mjuQr4BAhQoV7IILLggZ6Pj6669d0CKcBg0auOc7bdq0wL6QX3/91RYvXpzt7Jtdu3bZe++957IttC8UrFCQY/To0WEfoywZBTS89auxt1deTPtDARIFLpQZpNdZQRL/ftR9pUuXth9//DFb2woAh6P8Rtu2bSk/BQCIKIx/AADAj6BGhPKXfEp/Oeecc4Lm1cHxcPOmP0Ctg8HetNxS0OC0005zgQmVO1KpKB1wnzBhQmCeb775xgUTFCTQQe/LLrvM9UQQnWU/ZcoUmzVrlgssfPzxx0HLf/75592B8XHjxrn+Cb169XJBkr179wbmeeutt+zdd9916y9SpIjddddd7n6VKtK8+ud6zpw57vEPPvigO3ie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lnTXL730Uo6Xpff5s88+a//8848VLlzYvd/0HPUe8Lz44os2fPhw27hxo9snL7/8slWsWNFNe+yxx+yNN96wJUuWWLFixeyCCy6wBx98MHBg65577rEHHngg6L00evRoO//883O1DwAAeetM1RkzZlizZs0sOjr6SG8OAACHBeMfAADIc5kaXbt2dQf2Fy1aZCNHjnQHdocNGxY0jwIK7dq1c2fKn3322da8eXN7/vnnM13uzp07rX379vbwww8fcBtGjRplBQoUCPnP0xlnnGF79+61X375xR2YVrbI3XffnenyLrzwQlfz+ttvv7XPP//cJk2aZIMGDcowX9GiRV0QxU8HonVgPtLodVIwYtWqVXbcccdZjx49Qs6XlJR02LZJgaebbrrJnRWr4FhOgiyeXbt22SOPPGJr16517w2956+66qrA9O+//95uvfVWGzNmjK1bt87Kly/v3kf+96LeGwp4qPSIAmMKZPideeaZbh96FwIaAHB00VgwZ84cyk8BACIK4x8AAMhzQY34+HirUKGCVa1a1WVIdOrUyQUD/CWAdIC7UaNG7gDzo48+arfddtsBl9uvXz8XfNDyMvPXX3+5M+ZfeeWVDNPGjx/vDh689dZbLsujW7dudv/997sz7hXoCGXu3Lku40Nn2bdu3doFVp5++ml777333AF7P2V9+Ne7e/duN5/uj1TKNFAQYeXKle4AvrJ59Pd5553nMhSUfbN9+3YXJFIWgy7KolAQS5TJoACV3jdetstTTz1l9evXd1kRyoDQa+TZtm2bXXPNNVa9enW3/FatWtny5cvdtCeeeMLq1q3rgk+1a9e2Z555Jmhb//jjDxds03IbNmxo7777btjnpWwfrVvPr1SpUm6bJ0+eHJj+6quv2kUXXeTeM0WKFHHZQD/++KML9okCHto2ZbMoo6l///5BjwcAHP2UnaexgvJTAIBIwvgHAADyXFDDb9asWS4jwv9jfcGCBe4gtrI3FPhQjwOVqNJB4tzS2fN9+/Z1QQoFVtJTSaQmTZq4s+Y9Xbp0cQfCdbZ9KHqMDnK3bNkycJ8CKypD9euvv2YIvPz000+uxJV89NFHVqNGDZeJkpk9e/a4bfBfjhZ6TRQQUpChdOnS7j4FCxTYUKBC18rY0ftC75e///7b5s2bZzfccEPI5SmjRxkOKgW2YcMG69Wrl5111lmB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fffdVrFiRbfcTp062fz584Pm8Z7T1KlTg+7fs2ePW5emEZwBAAB+UVFRVqdOHXcNAECkYPwDAAB+2f5FvGTJEpsxY0bQfd9//701b97cqlevbldccYXt3LnTDqauXbva6tWrbdGiRTZy5Eh78cUXbdiwYUHz/PDDD9auXTsbPHiwnX322W57nn/++UyXO2TIEPv666/trbfesrlz59r111/vghyfffZZYJ4bbrjBxo0bZ2PGjLEff/zRVq1aZb169cp0uY888og99dRTLkDy66+/WpEiRaxLly4ZAjFVq1a1V199Nei+Tz75xAVPAAAA0tPJD0888YS7BgAgUjD+AQCAXAU1LrvsMnvppZcCf69bt84FEXQgXgf733vvPbv99tvtYIqPj7cKFSq4IEDPnj1d5sO3334bmL5lyxbr0aOHa5x500032aOPPmq33XbbAZf7yy+/2MUXX2wdOnSwGjVq2KBBg6xZs2b222+/uelbt2610aNHu4MHp556qrVo0cIFIfS49BkW/iyNUaNG2Z133um2qWnTpvbGG2+4YMjYsWOD5tW6tb92794duO+VV15x9wMAAKSnrNXevXu7awAAIgXjHwAAyFVQ488//3S1nD0fffSRC2h89913Lovi6aefznDw/mCaNWuWCyrExcUF7luwYIFt377dZW8o8KGyDPrBf+WVV2a6rBNOOMFlZaxcudIFI5Tt8e+//wae37Rp0ywpKckFUTz169e3atWq2ZQpU0Iuc/HixbZmzZqgxxQvXtxat26d4TEKkiiYon0oy5Yts0mTJlm/fv2ydKbKtm3bgi4AAODoL7+h/3UoPwUAiCSMfwAAwC/LXSYvueQSd71582Z7+eWX7dNPP3WBAJVXio6OdmWnvOwGZSVceuml7m9lVnTv3t1y4/PPP3eBk+TkZHcwX//QPPPMM4Hp9erVszJlytjQoUNdwEGBgqxQAEbZGeqpocZjWu7//d//2UknneSmKzih4EmJEiWCHle+fHk3LRTvfs2TlcdoPyk746KLLnJNzk8//XQrW7bsAbf9oYcesnvvvTdLzxMAABxd5TdUQlOZrAAARALGPwAAkKOgxj333OOCGOotcd555wUO/Cvb4brrrrMLLrggkDUxfvz4wPzpAwI5ccopp7j+GOrVoWwQBSDUsNtTtGhR19dD63z22WddPws9Rgf9jzvu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",
      "text/plain": [
       "<Figure size 1600x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig, ax = plt.subplots(figsize=(16, 6))\n",
    "\n",
    "cores = [\"#185FA5\"] * 12 + [\"#D85A30\"] * 12\n",
    "ax.bar(mensal[\"mes_str\"], mensal[\"receita\"] / 1e6,\n",
    "       color=cores, edgecolor=\"none\", width=0.7, alpha=0.85, label=\"Receita real\")\n",
    "\n",
    "ax.bar(meses_2025, proj_2025 / 1e6,\n",
    "       color=\"#534AB7\", edgecolor=\"none\", width=0.7, alpha=0.75, label=\"Projeção 2025\")\n",
    "\n",
    "todos_x = pd.DataFrame({\"mes_idx\": range(36)})\n",
    "tendencia_completa = modelo.predict(todos_x)\n",
    "todos_labels = list(mensal[\"mes_str\"]) + meses_2025\n",
    "ax.plot(todos_labels, tendencia_completa / 1e6,\n",
    "        color=\"black\", linewidth=1.5, linestyle=\"--\",\n",
    "        label=f\"Tendência linear (R²={r2:.2f})\")\n",
    "\n",
    "ax.axvline(x=11.5, color=\"gray\", linewidth=0.8, linestyle=\":\")\n",
    "ax.axvline(x=23.5, color=\"gray\", linewidth=0.8, linestyle=\":\")\n",
    "ax.text(5.5,  155, \"2023\",         ha=\"center\", fontsize=11, color=\"#185FA5\", fontweight=\"bold\")\n",
    "ax.text(17.5, 155, \"2024\",         ha=\"center\", fontsize=11, color=\"#D85A30\", fontweight=\"bold\")\n",
    "ax.text(29.5, 155, \"2025 (proj.)\", ha=\"center\", fontsize=11, color=\"#534AB7\", fontweight=\"bold\")\n",
    "\n",
    "ax.set_title(\"Receita Mensal 2023–2024 e Projeção 2025 — Regressão Linear\")\n",
    "ax.set_ylabel(\"Receita (R$ milhões)\")\n",
    "ax.yaxis.set_major_formatter(mt.FuncFormatter(fmt_milhoes))\n",
    "ax.xaxis.set_tick_params(rotation=45)\n",
    "ax.legend(loc=\"upper left\", fontsize=9)\n",
    "ax.set_ylim(0, mensal[\"receita\"].max() / 1e6 * 1.15)\n",
    "\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "06a8ef79-4b3a-4aa1-92e7-2c4c05eed7c8",
   "metadata": {},
   "source": [
    "## simulação de cenários de câmbio"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "ee47cfa4-8b1a-4148-94c4-f2db44314951",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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b97cZs+eHQ627tixw6644gq7/vrrXYC3QoUKVqxYMfvnn3/ifd8bb7zR/V23bl3M53fu3OmCqq+88opddNFFbty0adNcxuyiRYusUaNG9umnn9rPP/9sn332mZUrV85OP/10e+ihh+y+++6zYcOGWd68ed3rcufObR06dLCpU6faueee68b9+eefrpSDAsOvvvpqKi4xAAAApAUybQEAAIAYli9f7jJavWCorF692nbv3u2ybxXUrVWrlrVv39569uyZomW4ePFiO3z4sAsSe0466SSXGetlzOrvqaee6gK2npYtW9quXbtsxYoVEe/XtWtXe/31123fvn3usTJyFWT2vzaWgwcPuvfzDwAAAEh/BG0BAACA//rwww9dPdn8+fO7AKnKDKhurKdOnTpWunRpGzBggK1atSrVltvmzZtdcLh48eIR4xVk1XPeNNFBV++xN42nQYMGVqNGDXvzzTctFAq5oK0CuQkZOXKkyxz2BgWmAQAAkP4I2gIAAAD/1axZM9dJ2DfffGM333yzdenSxXUI5ilSpIh9/vnnLoN14sSJ1rZtW7v88svtxx9/DNwyVJBWJRZUH1c1dVu3bp3gawYOHOhKNXjDhg0b0mVeAQAAEImgLQAAAODrxEslD0477TRXE1bBW9Wa9VMG7ltvvWXjx493tW6Vkapg799//53s5ag6uupgTDVz/bZs2RKusau/ehz9vPdctI4dO7p6uKp3q5q6qnWbmJq+RYsWjRgAAACQ/gjaAgAAALEayjlz2qBBg2zw4MG2f//+mMuoXr169vTTT7us1KVLlyZ7OTZs2NDy5Mljc+bMCY9buXKlrV+/PtyZmP4uW7bMlWzwqJM0BVY1H9FKlizpsoCVaZuY0ggAAAAIDoK2AAAAQBzUyViuXLlcKQT54YcfXOaqAqpHjhxxmbFjxoxxNXBjBU4927Ztc2UXfv75Z/dYr9djrxatsnW7detmffv2tblz57qOyVSaQYHaRo0auWlatGjhPkNZsz/99JN98sknLqDcq1cvlyEbi2rZ/vPPP65TMwAAAGQeCd8jBQAAAGRTKilwxx132OjRo61nz55WoUIFV+e1VatWtnHjRhfQrVu3riuXoOfi8v7777sgrOf66693f4cOHeqCwDJu3DiX3asaugcPHrSWLVu6LF6PPksdpWk+FMxVKQfV3R0+fHicn1ugQAE3AAAAIHPJEVJ3soiwa9cul+2g29zSo45XlWn9WQPJsL7LaJYbAADIMMpirVatmjVt2jTLroX0bhcLbePkoW0MAEDWQnkEAAAAAAAAAAgQyiMAAAAAydC5c2eWGwAAANIEmbYAAAAAAAAAECAEbQEAAAAAAAAgQAjaAgAAAAAAAECAELQFAAAAAAAAgAAhaAsAAAAAAAAAAULQFgAAAAAAAAAChKAtAAAAAAAAAAQIQVsAAAAAAAAACBCCtgAAAAAAAAAQIARtAQAAAAAAACBACNoCAAAAAAAAQIAQtAUAAAAAAACAACFoCwAAAAAAAAABQtAWAAAAAAAAAAKEoC0AAAAAAAAABAhBWwAAAAAAAAAIEIK2AAAAAAAAABAgBG0BAAAAAAAAIECyXNB22LBhliNHjojhpJNOyujZAgAAAAAAAIBEyW1Z0Mknn2yfffZZ+HHu3FnyawIAAAAAAADIgrJkNFNB2vLly2f0bAAAAAAAAABAkmW58giyatUqq1ixotWoUcM6duxo69evz+hZAgAAAAAAAIDsmWl7zjnn2PTp061OnTq2adMme/DBB+3888+35cuXW5EiRWK+5uDBg27w7Nq1Kx3nGAAAAAAAAACycND20ksvDf9fv359F8StWrWqvf7669atW7eYrxk5cqQL7gIAAAAAAABARsuS5RH8ihcvbrVr17bVq1fHOc3AgQNt586d4WHDhg3pOo8AAAAAAAAAkG2Ctnv27LHff//dKlSoEOc0+fLls6JFi0YMAAAAAAAAAJARslzQ9p577rH58+fbunXrbMGCBdauXTvLlSuX3XDDDRk9awAAAAAAAACQ/Wra/vnnny5A+++//1qZMmWsSZMmtmjRIvc/AAAAAAAAAARdlgvavvbaaxk9CwAAAAAAAACQbFmuPAIAAAAAAAAAZGYEbQEAAAAAAAAgQAjaAgAAAAAAAECAELQFAAAAAAAAgAAhaAsAAAAAAAAAAULQFgAAAAAAAAAChKAtAAAAAAAAAAQIQVsAAAAAAAAACBCCtgAAAAAAAAAQIARtAQAAAAAAACBACNoCAAAAAAAAQIAQtAUAAAAAAACAACFoCwAAAAAAAAABQtAWAAAAAAAAAAKEoC0AAAAAAAAABAhBWwAAAAAAAAAIEIK2AAAAAAAAABAgBG0BAAAAAAAAIEAI2gIAAAAAAABAgBC0BQAAAAAAAIAAIWgLAAAAAAAAAAFC0BYAAAAAAAAAAoSgLQAAAAAAAAAECEFbAAAAAAAAAAgQgrYAAAAAAAAAECAEbQEAAAAAAAAgQAjaAgAAAAAAAECAELQFAAAAAAAAgAAhaAsAAAAAAAAAAULQFgAAAAAAAAAChKAtAAAAAAAAAAQIQVsAAAAAAAAACBCCtgAAAAAAAAAQIARtAQAAAAAAACBACNoCAAAAAAAAQIAQtAUAAAAAAACAACFoCwAAAAAAAAABQtAWAAAAAAAAAAKEoC0AAAAAAAAABAhBWwAAAAAAAAAIEIK2AAAAAAAAABAgBG0BAAAAAAAAIEAI2gIAAAAAAABAgBC0BQAAAAAAAIAAIWgLAAAAAAAAAAFC0BYAAAAAAAAAAoSgLQAAAAAAAAAECEFbAAAAAAAAAAgQgrYAAAAAAAAAECAEbQEAAAAAAAAgQAjaAgAAAAAAAECAELQFAAAAAAAAgAAhaAsAAAAAAAAAAULQFgAAAAAAAAAChKAtAAAAAAAAAAQIQVsAAAAAAAAACBCCtgAAAAAAAAAQIARtAQAAAAAAACBACNoCAAAAAAAAQIAQtAUAAAAAAACAACFoCwAAAGSg6dOn27x581gHAAAAyPpB24kTJ1q1atUsf/78ds4559i3336b0bMEAACAbKBz586WI0cON+TJk8eqV69u/fv3twMHDqT4vUOhkA0ZMsQqVKhgBQoUsObNm9uqVasipvE+e9GiRRHjDx48aKVKlXLPESQGAAAItiwZtJ0xY4b17dvXhg4daj/88IOddtpp1rJlS9u6dWtGzxoAAACygVatWtmmTZtszZo1Nm7cOHvmmWdc29Rv7ty51rhxY7v77rutXbt2dsYZZ9ikSZPifd/Ro0fbE088YZMnT7ZvvvnGChUq5Nq50QHhypUr27Rp0yLGvfPOO1a4cOFU/JYAAABIK1kyaDt27Fjr3r27denSxerVq+catQULFrSpU6dm9KwBAAAgG8iXL5+VL1/eBU+vvPJKlxE7e/bs8PM7duywK664wk4++WS75557bMyYMTZw4MAEs2zHjx9vgwcPdq+tX7++vfDCC/bXX3/Zu+++GzHtzTffbK+99prt378/PE5tYY0HAABA8OW2LObQoUO2ePHiiEZvzpw5XUN54cKFMV+jW8U0eHbt2hXxV3Rrm25BU8P38OHDEQ1yDXv37rWjR4+Gx6ssQ968eW3Pnj127Nix8HgFj3Pnzh3x3sf2H7Qc+fLoXjYLHTgUMW858udVC91CB//3me47FchnoaPHLHTINz5HDsuZP6+Fjhy10OEjvolzWM58ed04PReWK6flzJvHjuk9jv5vHnPkzmU58uS2YwcPmR0L/W98ntzuuWOax5BvfN48liNXTvc9IuY9jb9TrHWXlutJlM2i7Wn37t0R44sUKeJer/f3K1q0qB05csT27dv3v1nPmdNluWhb9WfF5MqVy70/34n1xLbH74l9BPvyrHh80mdmV8uXL7cFCxZY1apVw+NWr17t1peybxXMVVmvpk2bxvs+a9eutc2bN7t2radYsWKuFJjauddff314fMOGDd17vvXWW9apUydbv369ffHFF66E2EMPPRTnZ2R0u1hCmoZ2cZLb+rQhaUNm1uNDVjzm8Z1YT2x7/J4Ss49IUCiL2bhxo6KJoQULFkSMv/fee0Nnn312zNcMHTrUvSa+oVu3bm5a/fWP12ulRYsWEeP/85//uPH16tWLGD9r1iw3vkiRIhHjly9fHtq5c+dxn6txes4/Tq8VvZd/vD5L9Nn+8Zq3WN+T75Q911Oh3Dkjxn/Quk7o+/anHvedNE7P+cfptb92OD30n6Y1IsbXKpbfjX/o7MoR4xuXL+LG9zqlXMT4a2qWdOP11z9e02m8Xucfr/fVeH1OxHdtWsONT8/vxO8p6dteRqynzLztZfQ+IrPu94Kyj2Dbi3s9ZSc333xzKFeuXKFChQqF8uXL575/zpw5Q2+++WZ4ml27doVKly4d6tSpU2jQoEGhuXPnJvi+X3/9tXuvv/76K2J8+/btQ9dee234saZ55513QuPHjw81a9bMjXvwwQdD7dq1C23fvt09H9fn0S7O3vvS7PadOD7QLk7vbY+2SdLbW+z3krft0S4+NUVt/fQ6PiUkx38bdlmGbg874YQTXDbDueeeGx6vzh/mz5/van8lJqNAt7Jt2LAhnBXClTWuFmaVq7qLr60fMY8FlHGdw2zvkWOR3zV3Tpdovd+XhS2F8+SyI8dCdsCfna3p8+SyQ0eP2SFfdrbet2Du48fnzpHD8ufOaQeOHLMjvl1Q3pw5LG+unLbvyFF/knd4/N7DR90eLvxdc+W03Dlz2J7DR9P0O1V99svweK6+J37bW3VLk3RdT1ll26szdQGZH8nY763tck6G7SMy87ZX+Zkv/jfvZNqmakdkGzdudPVptb2qpq2Owc8991zEdMuWLbNhw4bZnDlz3DbdrFkze/DBB61BgwYx31ftW9XAVXtXHZF5rr32Wte5mPp1EP2v+rXnn3++VapUyVasWOGyc1ULt0mTJlaiRAlXTzdWZi/tYrLoslO2I+3i5B3zTnzuq3RdT1ll21PbmLZJ0ttbZ7y+lIzoZGx7P1xbn3bxkaS39b39W3rtIxKS5YK2WqDaub/55puufphH9btUO+y9995L8D10UNCtZjt37szWt/Iha1rZMfaJIOJW5+UfWTxsa+mG7S152LexvQUtaKt2p1dnVifs6hi3d+/e1q1bt+Omnz59ugsmqMTBBx98YKtWrbIyZcocN506NatZs6b9+OOPdvrpp4fHX3jhhe7xhAkTIoK2agu3b9/e/vnnH1u5cqVLSFCQI76gbTTaxcjKOHYkD20Vtrf0xPbG9padt7cs1xGZItWq4aWMBY8aynrsz7wFAAAA0oOyNQYNGuQ6EPN3DOanznOffvpplzSwdOnSmNNUr17ddW7mb+cqqKo7yeJq53bt2tXmzZtnN910k8sOAQAAQOaQ5YK20rdvX/vPf/5jzz//vP3yyy/Ws2dPl4rcpUuXjJ41AAAAZEPKeFXQVB2ByQ8//OBKIygDVrftKjN3zJgx7nY5BXBjUQatsnVHjBhh77//viuvoGBsxYoVI+4w82vVqpX9/fffNnz48DT9fgAAAEhduS0Luu6661zjdMiQIa6HXd0uNmvWLCtXrlxGzxoAAACyIdVlvOOOO2z06NEuoUA1aVWuQEFV1b9VQLdu3br21ltvRdSrjaZ+GpSM0KNHDxfoVY1atXMV7I0r0Fu6dOk0/GYAAABIC1mupm1qoHYXsjJqd2X+ujaZBdta8rC9sb2lJ7a3YFBN22rVqiWqxmx6o12MrIy2SvJw7GB7S09sb2xv2Xl7y5LlEQAAAAAAAAAgs8qS5REAAACAzKJz584ZPQsAAAAIGDJtAQAAAAAAACBACNoCAAAAAAAAQIAQtAUAAAAAAACAACFoCwAAAAAAAAABQtAWAAAAAAAAAAKEoC0AAAAAAAAABAhBWwAAAAAAAAAIEIK2AAAAAAAAABAgBG0BAAAAAAAAIEAI2gIAAAAAAABAgBC0BQAAAAAAAIAAIWgLAAAAAAAAAAFC0BYAAAAAAAAAAoSgLQAAAAAAAAAECEFbAAAAAAAAAAgQgrYAAAAAAAAAECAEbQEAAAAAAAAgQAjaAgAAAAAAAECAELQFAAAAAAAAgAAhaAsAAAAAAAAAAULQFgAAAAAAAAACJHdGzwAAAACQVHv37rUtW7bY/v37rVSpUla+fHkWIgAAALIMgrYAAADIFJYtW2bTp0+32bNn288//2yhUCj8XLFixey8886z9u3bu6FgwYIZOq8AAABASlAeAQAAAIG2cOFCa9q0qZ122mn29ddfW/PmzW3KlCn2/vvv2yeffGIzZsywQYMGWeHCha1fv352wgkn2MMPP+yycQEAAIDMiExbIJup8/KPGT0LAAAkSZs2beyuu+6yF154wapUqRLvtEeOHHGB3LFjx9qxY8fsgQceYGkDiIl2MQAgyAjaAgAAIND++OMPl0WbGLlz57bLLrvMDWTaAgAAILOiPAIAAAACLbEB22iFChVK9XkBAAAA0gNBWwAAAGQaixcvtjlz5oQfb9++3bp3725NmjSxYcOGuZIIAAAAQGZH0BYAAACZRp8+feyrr74KP+7du7e9/vrrVr58eXvsscdcB2QAAABAZkfQFgAAAJnGzz//bGeffbb7f//+/fbmm2/a+PHj3d9Ro0bZiy++mNGzCAAAAKQYQVsAAABkGvv27bOCBQu6/7/++ms7ePCgXXHFFe5x/fr17c8//8zgOQQAAABSjqAtgFSxe/dud4tqw4YNrXTp0lagQAGrXbu2PfDAA+651HjtypUrrVmzZq5Dmho1atj06dMj3ke3x+pE/vfff2etAkAWpf3/zJkz3f8vv/yyO3aULFnSPd66dasVLVo0g+cQAAAASDmCtgBSxb///msTJkywFStWWKVKlVxgddWqVTZixAi77rrrUuW1Xbt2tWXLlrnnzj//fOvWrZv9+uuv4Y5o7rrrLtcJTc2aNVmrAJBF9e3b10aPHm1lypSxF154we6+++7wc/PmzXPZtgAQBGqXagAAIDkI2gJIFfnz57cxY8bY33//bUuWLLENGzZYo0aN3HPKiFJQNaWv1XN16tSxChUqWOPGjV0P4cuXL3fP3XPPPVaxYkV3Mg8AyLp0AU/B2QEDBthnn31mHTp0CD9XqlSpiCAuAKSmatWqWY4cOdyQM2dOd/HokksusW+//TZiOtXYrlevnusYcfjw4XbCCSdY+/btk/x5Sl7Qa/Ply+fuKFD798MPPww/r7reV111lZvGmy/tH/06d+4cfk77T7/WrVuHn9M+FQAQLLkzegYAZA3qtVuBU38g9qyzzrJFixa5Rm3u3LlT/NrTTz/dlUjYtGmTq2Oo50455RSbO3euy7b65ptv4v0cAEDWcMEFF7ghGhltANLDRRddZHXr1rU5c+a4i0c//fSTbd682bVN16xZ4y4mFSlSxGX+KyBarlw5+/zzz5P8OXov7etKlChhCxcutAULFli7du1s7dq17u60Q4cO2ffff+/aze+9916C7/fqq6+6RAld4NKda7NmzUrmEgAApAeiGwDShOoKvvXWW+7/66+/3jVcU/raqVOn2q233mq1atVyjd/nnnvOZTy0bdvW+vTp41536qmn2saNG+3CCy+0yZMnu+kAAFnL4cOHbcqUKfbdd9+5uzMmTpxoJ554os2YMcMFSRRMAYC0oqzZ2267zd0F1qBBA3e3mNqflStXtsWLF7t91E033WTFihULX1BSJ4pJpX2cv5yY+n44cuSIrV+/3gVt9f76/8CBA65PiPgoU3fbtm2u/Xzfffe5/WYoFAqPBwAED0FbAEn2ww8/2O233x4xTlmxHnUEdumll9pff/3lbuNS8DSx4nutSiNE3/KlW7nU4OzVq5fLulXQ9vnnn3e3iukW2ddee401DABZiDLPmjdvbv/8848Llnz11VfhTiu/+OILlzk2bdq0jJ5NAFmcgqde+7ds2bLuzjGpUqWK+6s2rEp3qa+F+fPnu/4YkuOpp56yX375xWXZSosWLeycc85J8vtcfPHFLgj89NNPu4Cz9pNnn322C/Zq/gAAwUPQFkCS7dq1y5UiiEW3bl1++eXuZFoZsAqaFixYMFHvm9TXKrth7Nixru7t0qVLbc+ePXbDDTe41yrTavbs2axdAMhi1Omk6kiqhmTx4sUtb9684ed0l8XAgQMzdP4AZH09e/Z0g+iurzfeeMPy5MnjHiugqj4Wxo8f7y4yaVCb9LzzznPlFFQGLNorr7wSURf3jjvucHeWefVxvaCqMmvbtGljuXLlSvI8q3SDki769+/vauWqPX/nnXe6zFsAQDDRERmAJGvatKnLbvUPXqNSNb4UdFUj8N133z0u6Kpbx0466SQ3vPPOO+HxiXmt39GjR6179+7WqVMnlzngzYN38u41nAEAWYvuuBg8eLC7TVi1Iv2U6aa65wCQltRmVRtU7c1169a5LH+/xx9/3O2LVNu2YcOGrhNdZcoquBvLp59+ahMmTAgPf/75Z8Q+T+UP1IeD2ru6cOVvQydFt27dXGbtJ5984kqIXXvttcl6HwBA+iBoCyBVqJyBGn5qVCpwqmwBZRQ0atTIDSqpIKrxpc7ENOzcuTNJr/VT9oLqGKpRLJquUKFCrtGrzhmUeatgLgAga1GHk96FumhbtmyxwoULp/s8Ach+NW1ffPFFGz16tHs8aNAg1y4V1ZjdsWOHK5mgWtvKjNXz3j4qlunTp0ckQyhBYu/evXbs2DH3fL58+VyHZAr+itq5yaH6tR07dnT/9+jRI+JOBQBA8FAeAUCqUO+13km0/o8un6BbsFLrtQrKDhkyxNXiUm+6ooaxOqDp16+fK42gDIgnnniCtQsAWYxKIOiCneqf63ZfUcatjiPPPvssF+wApBuVG1AiwR9//GGjRo1y9Wc///xzV95AQVZ1kqv9k/6KasgmlkoqqM8G1cJVsFX1aJX0oPdTXW9P586d3R1onkcffdQFgW+55RZr0qTJce/78MMPu/IIZ555Zoq/PwAgbRG0BZAqVM8rrsynhKZL7Gs91atXd9kH0S677DI3AACyLgVGdDdGvXr1XB10BTDUC/ry5ctt1apVEXUhASAtKVP1/vvvd1mrU6ZMcf+fddZZ1rJlS9dJmZdZW7VqVRfcVSA3Ke1d1bX97LPPXAJDqVKl3MWqPn36uM56PeqA10+lD0TZurGCtkp08Ad9AQDBlSOUlEhJNqGDooq869btokWLZvTsAECmtLJjg4yehUypzss/ZvQsZEpsb9lre9MdF8OGDXOZaKqFriw0BSEefPBB11M7Ug/tYiD5tJ/y/0X2Rlsle7VVMhrbW9bY3si0BQAAQKaiDLTo7DIACBqCtQCAlCBoCwAAgExHN4v99ttvtm3bNnfbsDr8UakEAAAAICv4/94bAAAAgEzi6aefdr2oq66tajvWrVvXKlasaJMmTcroWQMAAAAyJtNW2Qzz5s1zvbtv2rTJ9u/f77Ib6tSp43q2pBdKAAAApKbbbrvNJk+e7P5/9tlnXc/sN9xwg+sBvVy5cq6znxkzZrjxefLkcb2mAwAAANkiaDt//nybMGGCffTRR3bkyBGrUqWKlS5d2vLly2e//PKLvfLKK7Znzx7XC3y3bt3szjvvpBMvAAAApNi0adPCQdtx48bZXXfd5Xpi97v88sutTJky9thjjxG0BQAAQPYoj9CiRQu74oorrESJEvbee++5bFv12vvdd9/ZV199ZcuXL7edO3fazz//7DIcNE2NGjXs448/TvtvAAAAgCzt8OHD9u+//7r/1QZt06ZNzOkuu+wyW7duXTrPHQAAAJBBmbZNmza1N954w4oVKxbnNOr44aSTTnJD37597csvv7Rdu3al5rwCAAAgG8qZM6dt3LjRleRSLduFCxda8+bNj5tu0aJF7nkAAAAgWwRtBw0alOQ3Vn1bAAAAIKUuueQSq1+/vvtfZbiGDx9uBw8etGuuucbVtN26datLMBgzZowNGTKEBQ4AAIDs1xFZNNW3/e233ywUCrnOyHLnTvFbAgAAAGEzZ84M/3///ffb9u3bXYB25MiR4fFqg6pPBT0PAAAAZHYpirAuXrzYrr76alu/fr17XLlyZXvzzTftrLPOSq35AwAAACJKcj3++OPuTrBvvvnGBXBLlixpZ599tiufAAAAAGSbjsjicvvtt7th9+7dtmnTJmvSpIn16NEj9eYOAAAAiEEB2tatW1vHjh3t0ksvJWALAACA7Jdp26dPH1c7rEiRIhHjV69e7W5DK1CggBUqVMhuvvlma9++fVrNKwAAAOCya1Uy4c8//7QDBw4cl4n7wAMPsJQAAACQ9YO2O3bssNq1a9vDDz9sXbt2DY9v3Lix3XjjjW7cvn377NFHH6UDMgAAAKSZTz/91HVAtmfPHpc4kDdv3ojnCdoCAAAg25RHmDZtmr333nv27LPPunphqh8m//nPfyxnzpwucHvrrbda9erV3TgAAAAgLfTr18/1n7B27Vrbu3evy7r1D9u2bWPBAwAAIPt0RKZg7aJFi1wAt127dnbJJZe4Xntff/31tJ1DAAAA4L/WrFljY8eOtapVq7JMAAAAkGUluSOyLl262MqVK6106dJ28skn22OPPWZHjhxJm7kDAAAAfM444wzbsGEDywQAAABZWqKDtqtWrbLJkyfbhAkTbPny5fb444/bl19+aXPmzLFTTjnFZs2aZUFQrVo1V8vMP6jWLgAAADK/SZMm2RNPPGGffPIJiQMAAADI3uURnn/+ebvlllvsxBNPtIIFC9o999xjt99+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wpUqW7x4sQvCKkirgLBfhQoV3Hz/+eefEeOnTp1qVapUSfK8AwAAIBMEbdWQvP76661mzZqWL18+++GHH9z4+++/32bOnJna8wgAAADEGQh94oknXKD166+/TvJSUlu2fPnyLmP1yiuvtObNm7uAqUfZsFdccYWdfPLJds8997gg6cCBA5O1Nnr37m0DBgywRo0axXz+l19+sVmzZtlzzz1n55xzjjVp0sSefPJJe+211+yvv/4K9y9x6NAhF3zVPKlNftddd9nYsWMj3qts2bIuuPv888+Hxy1YsMD++ecfu+yyy5I1/wAAAAhw0FaN2AYNGtgff/zhMgEOHz4cfk63lT399NOpPY8AAACA9enTx2699dbwkgiFQtasWTPr16+fPfXUU3bhhRfajBkzkr2kli9f7gKbefPmDY9bvXq168NBQWEFdmvVqmXt27e3nj17pvoaWbhwoSuJcOaZZ4bHKYicM2dO++abb8LTXHDBBRHz2LJlS1u5cqVt37494v26du3q6vB6FOhV+93/2mgHDx502bz+AQAAAJkgaKvMAl3RV4NxyJAhEc8pmPvjjz+m5vwBAAAAzjvvvBORpfrBBx/YkiVL3F1f//77r91yyy326KOPJmlpqQRB4cKFXX3YU0891bZu3Wr33ntv+Pk6depY6dKlXYbsqlWr0nRNbN682WXI+uXOndtKlizpnvOmKVeuXMQ03mNvGk+bNm1c0FUlFvbu3Wuvv/66C+TGZ+TIkVasWLHwoEA1AAAAMkHQVhkIN954o/tfnRj4KTNAt1wBAAAAqUVBx/nz57sSAcp61WMNr776qtWrV89lmOqxMlR/++238PPr169P8L2VqavArzJZb775ZuvSpYtdffXV4eeLFClin3/+uSvDMHHiRGvbtq1dfvnl8SYqPPLIIy4Q7A2JmY+0oLvgOnXqZNOmTbM33njDateubfXr108wQWPnzp3hYcOGDek2vwAAAPif3JZEutLv1dSKpkayOj0AAAAAUos61JJjx47ZsmXLwmUANF53ennPq/6sSnfNmzcvXDohoU63ChUq5EoeeOUDTjvtNJsyZYp169YtPI0ycN966y1XakDBW91xpvdW5m2ZMmWOe8/bbrvNrr322vDjihUrJup7qrauMn39jhw5Ytu2bXPPedNs2bIlYhrvsTeNnzJrVR9XiRcJZdl6NX41AAAAIJMFbdVBg2p66dY0r4GrjFvdjvXYY49FZCYAAAAAKaW2p6hTLd3Zpce//vqrPfzwwzZo0CA7//zz3fPqiEzB1egSXoml2rF6v759+1qHDh2sQIECx02jzF7ddfbSSy/Z0qVL7eKLL46Z5KAhqc4991wXeF68eLE1bNjQjVOWr4LVCrx606jzXwWnlUnr9TmhMg4lSpQ47j3VWZkGzau+EwAAALJoeQTVuVJGgW6t8hqPumqvhqLqXg0bNiwt5hMAAADZXK9evezxxx+3atWquaCmyiF4AVuZNWuWnX322Sn6DHUylitXLlcKQVQvV+1bdfSlrFcFVceMGeNq4CqAmxRKclApBnVuJsoa1mNl0krdunWtVatW1r17d/v2229dEPqOO+5w/Ul42boKvKojMWUCr1ixwnW8NmHCBBdojosCv5s2bXIBbwAAAGTRTFsFZtWrrrILdFXfyyRQI/qmm26KtzdaAAAAILn69evnAraqV6uSXGp/+u3Zs8fuvPPOFC1gdfylQOno0aOtZ8+e7nNU11XB1I0bN7qAroKryuhNalmwyZMn24MPPhh+fMEFF7i/qjnbuXNn9//LL7/sPl8ZvMr81V1sTzzxRERb/NNPP3XfXYFrdZKmzOIePXrEWwICAAAAmUuOkAp+IYJ62VWDWJ0vFC1alKUDAMmwsmMDllsy1Hk57s6NwPaW2tjekkY1bRU0btq0abb5OdIuBoDUQds4eWirsL1l5+0tyeURAAAAgCBSB2XDhw/P6NkAAAAA0j9oq9u0dFtYrEG3k5UqVcrdzvXBBx+kfO4AAACA/9qyZYt99913tnXr1ohlorIFffr0sSpVqtiIESPSbHmphEF2yrIFAABAJgraquOFSpUqWa1atVzjWB2T9e7d22rWrOk6SFB9LfVme+WVV9prr72WNnMNAACAbJVBe9lll7m2ZqNGjeyEE05wtWuPHTtm999/v2uXPvXUU679uXz58oyeXQAAACD9OyJT77bqqffNN9+0HDlyhMc/9thjrqOE/fv3u84h1MvtqFGj3F8AAAAguYYNG+Y6wL3lllusQYMGtm7dOtep19KlS+3LL7+0tm3busSC2rVrs5ABAACQPYO2U6ZMcZ0w+AO2osfqtfamm25yjeYOHTrYddddl5rzCgAAgGzo448/tsGDB9uQIUPC45o0aWKXX365de/e3Z555pkMnT8AAAAgw8sj7Nu3z9avXx/zuT/++MMOHDjg/i9UqJDlzZs35XMIAACAbE1tz+hashdddJH726lTpwyaKwAAACBAmbbKaBgwYIAVLlzY3YpWpEgR2717t7333ntuvGqJybJly1x9MQAAACAl1F9C/vz5I8bly5cvnCgAAAAAWHYP2j799NOu51xlNagkQp48eVxDOhQKWbt27VwnEKLee9VJGQAAAJBSr776qn311Vfhx+qETG3Rl19+2ebNmxcer3HqLBcAAADIVkHbokWL2ttvv22//PKLfffdd7Zp0yarUKGC65ysXr164emuuuqq1J5XAAAAZFMTJkyIOX7cuHERjwnaAgAAINsFbVWv9pxzznEdjbVo0cLq1q2bdnMGAAAA/DerFgAAAMhOktQRmWqJbdy40XLmTHL/ZQAAAAAAAACAREhy9FVlD15//fWkvgwAAABIln///TdZr9u2bRtLHAAAANmjpm3jxo1t0KBB1qZNG2vdurWVK1fO1Q7zo54tAAAAUkv16tWta9eubqhfv3680+7du9feeecdVwP3yiuvtPvvv58VAQAAgKwftO3SpYv7qw7IPv744+OeVwD36NGjqTN3AAAAyPa+/vpre+CBB6xBgwZWs2ZNO++881zwtkyZMpYvXz7bsWOHrV271hYvXuymLV68uN1333122223ZftlBwAAgGwStFWDGAAAAEgvp556qr377ru2Zs0ae+GFF2zOnDk2Y8YMO3jwYHiaKlWquDvCXnrpJWvbtq3lzp3kZi4AAAAQGEluzVatWjVt5gQAAACIR40aNWzYsGFukO3bt9uBAwesZMmSLuMWAAAAyCpSlIKwb98+11COpoYzAAAAkJZKlCjBAgYAAECWlOSgbSgUshEjRtgzzzzj6trGQk1bAAAAAAAAAEienEl9wbhx42zs2LHWq1cvF8BVj7xDhgyx2rVrW7Vq1ew///lPMmcFAAAAAAAAAJDkoO2UKVPswQcftP79+7vHV155pQ0dOtRWrFhhdevWtdWrV7NUAQAAAAAAACC9grbr1q2z008/3XLlymV58uSxHTt2/P8b5cxpt99+u02fPj258wIAAAAAAAAA2V6Sg7alSpWyPXv2uP+rVKliP/zwQ/i5f/75x3VOBgAAAAAAAABIp47IGjdubN999521bt3aOnToYMOGDbPNmze7rFvVs7344ouTOSsAAABAwjZu3Gjjx4+3r776yrZt22YlS5a0888/3+6++2474YQTWIQAAADIfkFbBWnVUJZBgwa58givvvqq7d+/3y655BJ78skn02I+AQAAAFu+fLldcMEFdvjwYdf2VNmuLVu22OTJk13fC1988YWdfPLJLCkAAABkr6BtnTp13CD58uWzCRMmuAEAAABIa/fcc4/VrFnTPv30UytRokR4/Pbt261Fixbu+ZkzZ7IiAAAAkL1q2gIAAAAZRSURBg8eHBGwFT2+//773fMAAABAtsi07dq1a6LfMEeOHO7WNAAAACC15c6d2w4ePBjzOY3PlSsXCx0AAADZI2g7ffp0K1KkiLsVLRQKJRi0BQAAANJC8+bNXUatatnWrl07PH7VqlX2wAMPuDq3AAAAQLYI2p577rm2aNEiO3r0qHXo0MGuv/56q1q1atrPHQAAAOAzduxYu/DCC61evXp2yimnWLly5Wzr1q22bNkyq1KlinseAAAAyBY1bb/++mtbu3atdezY0V599VWrUaOGNWnSxJ5++mn7559/LL08/PDDdt5551nBggWtePHiMadZv369XXbZZW6asmXL2r333mtHjhxJt3kEAABA2lFgVgFaBWeVaXvs2DH3d9y4cbZ06VKrXLkyix8AAADZpyMyNZD79+9vS5YscQ3lZs2a2fjx461ixYp26aWXpksvvYcOHbL27dtbz549Yz6vTGAFbDXdggUL7Pnnn3elHYYMGZLm8wYAAIC0deDAAbv88svthx9+sLvuustef/11mz17ts2YMcPuvPNOK1y4MKsAAAAA2Sto66fb0R566CGXzdC7d2/XWP7Pf/5jae3BBx+0Pn362Kmnnhrz+U8//dR+/vlne+mll1ydMwWTNZ8TJ050gVwAAABkXvnz57f58+e7C/UAAABAVpbkoK0aycqqvfnmm618+fI2depU69atmw0cONAy2sKFC11AV7XNPC1btrRdu3bZihUrMnTeAAAAkHItWrRwF+oBAAAAy+4dkckXX3zh6tm+8cYbdvDgQbviiivs5ZdfdkHR3LkT/TZpavPmzREBW/Ee67m46Pto8CjICwAAgODp0qWL3XrrrbZ7925r3bq1a+vlyJEjYpozzjgjw+YPAAAASA2JiraqQwd1OKZyA5MmTbK2bdu629NSw4ABA2zUqFHxTvPLL7/YSSedZGll5MiRrvQCAAAAgq1NmzburzrE1eAP2IZCIfeY8gkAAADIFkHbjRs3Wp48eVzt2s8++yzeadVQ3rlzZ6JnoF+/fta5c+d4p6lRo0ai3kvlGr799tuIcVu2bAk/FxeVdujbt29Epi09DwMAAATP3LlzM3oWAAAAgGAEbYcOHZpmM1CmTBk3pIZzzz3XHn74Ydu6dauVLVvWjVOguWjRoq7ztLjky5fPDQAAAAi2Cy+8MKNnAQAAAMj6QdukWL9+vW3bts391W1vS5YsceNr1aplhQsXdh1TKDh744032ujRo10d28GDB1uvXr0IygIAAGQBP/30k7sLTPVso3388cdWqVIlq1+/fobMGwAAAJBaclomMmTIEGvQoIELIu/Zs8f9r+H77793z+fKlcs+/PBD91dZt506dbKbbrrJhg8fntGzDgAAgFTQp08fW7hwYcznVCZLpbcAAACAbJFpGxTTp093Q3yqVq3qsiwAAACQ9ehOq/79+8d8Thftn3zyyXSfJwAAACBbZ9oCAAAgezt48KAdOnQozucOHDiQ7vMEAAAApDaCtgAAAMg0VBrrhRdeiPmcxp922mnpPk8AAABAti6PAAAAgOxt4MCBdvnll9tll11mXbp0sYoVK9pff/1l06ZNs08++cTee++9jJ5FAAAAIMUI2gIAACDTULD2lVdesXvvvdeuvfZay5Ejh4VCIatUqZIbr+cBAACAzI6gLQAAADKV6667zg0rV660f//910qVKmV16tTJ6NkCAAAAUg1BWwAAAGRKBGoBAACQVRG0BQAAQKYxfPjweJ9XuYQHHngg3eYHAAAASAsEbQEAAJBpjBs37rhxe/bssaNHj1qBAgUsX758BG0BAACQ6eXM6BkAAAAAEmv79u3HDfv377eZM2darVq1bN68eSxMAAAAZHpk2gIAACBTy507t7Vs2dI2btxoPXv2tK+//jqjZwkAAABIETJtAQAAkCVUqlTJlixZktGzAQAAAKQYQVsAAABkemvXrrVRo0ZZzZo1M3pWAAAAgBSjPAIAAAAyjSJFiliOHDkixh0+fNgOHTpkBQsWtLfffjvD5g0AAABILQRtAQAAkGn069fvuKBt/vz5XWmESy+91EqWLJlh8wYAAACkFoK2AAAAyDSGDRsW53N//vmnzZo1yzp06JCu8wQAAACkNmraAgAA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f//9t33++efu+VNPPdVy585tS5cutf79+9vo0aMTDNq++OKLtmfPHitatGjMaX799Ve75ZZb7MILL3TBWr13ly5dws+/8sorNm/ePJs8eTLrDgAAAMiCCNoCAAD8V/78+V22rIKyS5YssQ0bNoSzYGfOnGnbt293/59yyiku81bB1e+//97Wrl1rBQsWdM99/fXX8S7PIkWK2F9//WV//vmnnX766TGnWbZsmcvYPe+886xixYpWp04d++mnn8KBZWUDP/TQQ1a9enXWHQAAANLMsGHD3ID0R9AWAADgv8qXL2/33HOPC6x6Qdyzzjrr/xtNOXO6jFrRXw0qUXDmmWe64Om+ffvcc02aNIl3eebKlcsqVKgQ7zTK3tXnLViwwAV4V65c6covSN++fa1atWp29913s94AAACQJGpHqjyXBrU3y5QpY5dccol9++23EdO9+eabVq9ePXv44Ydt+PDhdsIJJ1j79u2TvLR1t5peq5JiJUuWtMaNG9uHH34Yfn727NnWqlWr8DS62013mG3atCk8jZIXmjdvbsWKFQvPe3zf64UXXgiP379/v5UqVSr83KxZsyyzIGgLAAAQh61bt9pbb73l/r/++uvDwVzP4sWL3aDsV1F5BA0ppXq3zz33nM2fP99OPPFEF8SdOnWqffbZZ/bqq6/apEmT3Oco+FulShUbNWoU6xAAAACJdtFFF9ntt9/u+nFQG7NNmzbhvhnWrFljHTp0sC1btlj9+vXtjDPOcHeIqTxYUum9LrjgAuvWrZtVrVrVJSW0a9fO3XXm3aWmgLESJW644QZ3Z9v06dPtqquuCr/H+vXrXRC3QYMGifrMp556KqKs2LZt2ywz+v90EQAAgGzmhx9+cA1Vv0WLFoX///333+3SSy91ma7KCIhVP3bz5s0uw3bu3LkuqPvYY4+5IKvq0aaUMgz8dWz1Oa1bt3aZwGrYjh071mU+aP4GDBjgMnGVpQAAAAAkRFmzt912mysJpmCoyoOps93KlSu7pITDhw+7znOV3SoqkeDdWZYU3333Xfh/JTooSHzkyBEXiFVW7TXXXOOSEbxSY16Ad9GiRS6AW6JECWvbtq0blCWrpIb4KJtXn/nNN9/YOeecY08++aQblxkDt2TaAgCAbGnXrl2uMecfPAsXLnS1bNUJmRqIn3766XFZth41MFUmQbeVKTthyJAh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2rdvX8T4TZs2hQoWLBi67bbbQhdeeGFIq9Y/yLRp00LFihULv2bo0KGh0047LTRlypRQ5cqVQ4UKFQr17NkzdOTIkdCoUaNC5cqVC5UpUyY0YsSIiM/S+73zzjvu/4MHD4Z69eoVKl++fChfvnyhKlWqhB555BH3XNWqVSPmQY9l9erVocsvvzxUtmxZ95lnnnlmaPbs2Wm+7JD2br755tAVV1wRMe7LL79063/r1q3ucf/+/UMnnnhiqECBAqHq1auHBg8eHDp06FB4+iVLloSaNm0aKly4cKhIkSKhM844I/Tdd99FvF+TJk1C+fPnd7+FO++8M7Rnzx5WbybdPi655JJQo0aNQgcOHAj169cvVLFiRbcvO/vss0Nz584NT7du3bpQmzZtQsWLF3fP16tXL/TRRx+557Zt2xbq0KFDqHTp0m67qFWrVmjq1KnuubVr17rt78cff3SP9Z56PGvWrNDpp5/upm/WrFloy5YtoY8//jh00kknue3uhhtuCO3duzf8+dqv3n333eHHEydOdJ+j/Z72ZVdffXX4O0bvfzUP2q927do1VK1aNfeZtWvXDo0fPz6NlziS49JLLw2dcMIJMfcr27dvd3+1Xp9++ulQ27Zt3fao46m3bWka73//oGlEx8Jx48ZFvGePHj3cdqTt6eSTTw598MEH4efffPNNt73nzZvXvfaxxx5jxQI+tI0RZLSNkdTtg7Yxgoa2ccZKWeoR0pWyaD/55BN7+OGHXdasnzLJOnbsaDNmzHBX6U4//XR3+2X37t3jfc/ff//dZs6c6bKI9P8111zjMhZq165t8+fPtwULFrhSDM2bN7dzzjnnuNc/8cQT9v7779vrr79uVapUcbenafBuAVXG0bRp09wVRGW8yZ49e6x169bueyhj94UXXnC3na5cudK9B7IOreuXXnrJ3QavUgmibEXdNqzyHspg0zaqcf3793fPaztu0KCBTZo0yW0zqkWaJ08e95y2UW1LI0aMsKlTp9rff/9td9xxhxu0nSHz0b5MpV20Dn/++Wd77bXX3LbxzjvvuHWtbeTEE090GY6HDh2yL774wt16rmkLFy7s3uOBBx5wj7UvK126tLsDYf/+/fF+rjJ8n3rqKZfxeO2117pB+6NXXnnFbbft2rWzJ5980u67777jXvv999/bXXfdZS+++KKdd955bt/85Zdf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HcsKCwslvmbNmiX7TU9P140bN9abN292ee24ceP0xIkTa/1eZO14u379ug4PD9cxMTH64MGDev/+/ToyMlIPHDiwxuOMi4vTPXr00Hv37tXfffed7ty5s05ISHCsZ/tmDVaIt927d8vsuIcOHdInTpzQa9eulVl98Z4GxhvZHXNj8uZ4Y25sb1bIVYC5sXewQrztZm6sWbS1gIiICL18+XKPJxJOoICAAP3666/L8zVr1ug+ffro1q1bax8fHymaTpo0SV+6dOmWirZGkQzHYdiyZYuOioqSbXEMKLzm5ua6vC4/P19HR0dLgTc4OFgvWrTohvfr0qWLzsrKqvXxkbXjDYlp165dpcDq7+8v752dne0x3jwVbY3ljzzyiPb19dWdOnWSWHZ25coVideqcUre3b4VFRXp4cOH65YtW8prxo8fr8+fP3/D+yN+DFiPIi1egzidMGHCDe/D9s0azB5vBw4ckOQVbVPz5s2lfUxLS9N//fWXy34Zb2R3zI3JW+ONuTGZPVcB5sbew+zxdoC5MYu2VpCTkyN/uOHKxM1Cj8L6gl6QoaGhurKyUtenTZs2yee8du1ave6X6sYu8YarhZ6uIpP94m379u2SfDhfca4PbN/MgfFG5B3Mdi4zN/Zudok35sbmYLZ4Y27s3Rhv5seJyCxg0KBB6vjx46qoqEgGhG5omzZtksGlq5sV8GaVl5erVatWyXgp1HDsEm/Y37Jly+p1n+Qd8fbyyy+7jH9UH9i+mQPjjcg7mPFcZm7svewSb8yNzcGM8cbc2Hsx3szPB5Xbhj4IIiIiIiIiIiIiIvpXo//+S0REREREREREREQmwKItERERERERERERkYmwaEtERERERERERERkIizaEhEREREREREREZkIi7ZEREREREREREREJsKiLREREREREREREZGJsGhLREREREREREREZCIs2hIRERERERERERGZCIu2RERERERERERERCbCoi0RERERERERERGRMo//Ab+kYah1DnXuAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 1400x600 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "receita_unit_media = df_analitico[\"preco_unitario\"].mean()\n",
    "usd_price_medio    = df_analitico[\"usd_price\"].mean()\n",
    "\n",
    "cenarios = {\n",
    "    \"Otimista\\n(R$ 4,80)\":   4.80,\n",
    "    \"Base\\n(R$ 5,40)\":       5.40,\n",
    "    \"Pessimista\\n(R$ 6,00)\": 6.00,\n",
    "    \"Crítico\\n(R$ 6,50)\":    6.50,\n",
    "}\n",
    "\n",
    "margens, lucros = [], []\n",
    "for taxa in cenarios.values():\n",
    "    custo_unit = usd_price_medio * taxa\n",
    "    m = ((receita_unit_media - custo_unit) / receita_unit_media) * 100\n",
    "    l = (receita_unit_media - custo_unit) * df_analitico[\"qtd\"].mean() * len(df_analitico) / 2\n",
    "    margens.append(m)\n",
    "    lucros.append(l / 1e6)\n",
    "\n",
    "nomes     = list(cenarios.keys())\n",
    "cores_cen = [COR_LUCRO if m >= 0 else COR_PREJ for m in margens]\n",
    "\n",
    "fig, axes = plt.subplots(1, 2, figsize=(14, 6))\n",
    "\n",
    "bars = axes[0].bar(nomes, margens, color=cores_cen, edgecolor=\"none\", width=0.5)\n",
    "axes[0].axhline(0, color=\"black\", linewidth=0.8, linestyle=\"--\")\n",
    "axes[0].set_title(\"Margem Estimada por Cenário de Câmbio (2025)\")\n",
    "axes[0].set_ylabel(\"Margem (%)\")\n",
    "for bar, val in zip(bars, margens):\n",
    "    offset = 0.3 if val >= 0 else -1.2\n",
    "    axes[0].text(bar.get_x() + bar.get_width()/2, val + offset,\n",
    "                 f\"{val:.1f}%\", ha=\"center\", fontsize=10, fontweight=\"bold\")\n",
    "\n",
    "bars2 = axes[1].bar(nomes, lucros, color=cores_cen, edgecolor=\"none\", width=0.5)\n",
    "axes[1].axhline(0, color=\"black\", linewidth=0.8, linestyle=\"--\")\n",
    "axes[1].set_title(\"Lucro Anual Estimado por Cenário de Câmbio (2025)\")\n",
    "axes[1].set_ylabel(\"Lucro (R$ milhões)\")\n",
    "axes[1].yaxis.set_major_formatter(mt.FuncFormatter(lambda x, _: f\"R$ {x:.0f}M\"))\n",
    "for bar, val in zip(bars2, lucros):\n",
    "    offset = 3 if val >= 0 else -18\n",
    "    axes[1].text(bar.get_x() + bar.get_width()/2, val + offset,\n",
    "                 f\"R$ {val:.0f}M\", ha=\"center\", fontsize=9, fontweight=\"bold\")\n",
    "\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5f743457-026d-4e08-97f9-f32ffeeb45db",
   "metadata": {},
   "source": [
    "## Conclusão\n",
    "\n",
    "A análise revelou que a empresa cresceu em receita (+4%) de 2023 para 2024,\n",
    "mas o lucro virou prejuízo de 32 milhões de reais devido à alta do câmbio em reais  ( 4,99 →  5,39).\n",
    "\n",
    "A projeção de receita para 2025 aponta 1,53 bilhão de Reais (+9% vs 2024),\n",
    "porém a sustentabilidade do negócio depende diretamente do câmbio:\n",
    "apenas com dólar abaixo de R $ 5,00 a operação retorna à margem positiva.\n",
    "\n",
    "## Principais achados:\n",
    "- Propulsão concentra 74% do lucro total\n",
    "- Motor Diesel Yanmar Velocity 37HP gerou o maior prejuízo: R$ 8,7 milhões\n",
    "- Câmbio é o principal fator de risco do negócio — mais que volume de vendas"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
