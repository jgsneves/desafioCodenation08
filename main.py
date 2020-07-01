
doc = '''
#%RAML 1.0
title: desafio-8
version: v1
mediaType: application/json

types:
  Auth:
    type: object
    discriminator: token
    properties:
      token: string

  Agent:
    type: object
    discriminator: agent
    properties:
      agent_id:
        type: integer
        required: true
        example: 12
      name:
        type: string
        required: true
        example: "João Gabriel"
      status:
        type: boolean
        required: true
        example: true
      environment:
        type: string
        required: true
        example: "Windows"
      version:
        type: string
        required: true
        example: "versao 1"
      address:
        type: string
        required: true
        example: "Rua Tal, número 1"
      user_id:
        type: integer
        required: true
        example: 1
    example:
      agent_id: 1
      user_id: 1
      name: "Nome de agente"
      status: true
      environment: "Windows"
      version: "versão 01"
      address: "Rua Tal, número 1"

  Event:
    type: object
    discriminator: event
    properties:
      event_id:
        type: integer
        required: true
        example: 1
      agent_id:
        type: integer
        required: true
        example: 1
      level:
        type: string
        required: true
        example: "Entretenimento"
      payload:
        type: string
        required: true
        example: "Payload"
      shelved:
        type: boolean
        required: true
        example: true
      date:
        type: datetime
        required: true
        example: "2019-12-03"
    example:
      event_id: 1
      agent_id: 1
      level: "level"
      data: "payload"
      shelve: true

  Group:
    type: object
    discriminator: group
    properties:
      group_id:
        type: integer
        required: true
        example: 1
      name:
        type: string
        required: true
        example: "Nome do grupo"
    example:
      group_id: 1
      name: "Nome do grupo"

  User:
    type: object
    discriminator: user
    properties:
      user_id:
        type: integer
        required: true
        example: 1
      name:
        type: string
        required: true
        example: "João Gabriel"
      email:
        type: string
        required: true
        example: "email@email.com"
      last_login:
        type: date-only
        required: true
        example: "2019-11-20"
      group_id: 
        type: string
        required: true
        example: 1

  Response:
    discriminator: response
    properties:
      mensagem:
        type: string
        example: "Mensagem da resposta"

securitySchemes:
  JWT:
    description: Autenticação JWT
    type: x-{other}
    describedBy:
      headers:
        Authorization:
          description: X-AuthToken
          type: string
          required: true
      responses:
        201:
          body: 
            application/json:
              description: Token gerado
        400:
          body: 
            application/json:
              description: Token expirado
    settings:
      roles: []

/auth/token:
    post:
      description: Return JWT
      body:
        application/json:
          type: Auth
          username: string
          password: string
      responses: 
        201:
          body: 
            application/json:
              description: Token gerado
        400:
          body: 
            application/json:
              description: Token expirado
      securedBy: [JWT]

/agents:
  get:
    description: Retorna lista de agentes
    responses: 
      200:
        body:
          type: Response
          example:
            mensagem: Lista renderizada
      401:
        body:
          type: Response
          example:
            mensagem: Sem autorização
      404:
        body:
          type: Response
          example:
            mensagem: Não encontrado
    securedBy: [JWT]
  post:
    description: Criação de novo agente
    body: 
      application/json:
        example: {
            "agent_id": 1,
            "user_id": 1,
            "name": "João",
            "status": true,
            "environment": "Windows",
            "version": "versão 1",
            "address": "Rua tal, número 1"
          }
    responses: 
      201:
        body:
          type: Response
          example:
            mensagem: Agente criado
      401:
        body:
          type: Response
          example:
            mensagem: Sem autorização para criar agente
    securedBy: [JWT]

  /{id}:
    get:
      description: Detalhe de Agente
      responses: 
        200:
          body:
            type: Response
            example:
              mensagem: Agente encontrado
        401:
          body:
            type: Response
            example:
              mensagem: Sem autorização
        404:
          body:
            type: Response
            example:
              mensagem: Agente não encontrado
      securedBy: [JWT]
    put:
      responses:
        200:
          body:
            type: Response
            example:
              mensagem: Agente modificado
        401:
          body:
            type: Response
            example:
              mensagem: Sem autorização
        404:
          body:
            type: Response
            example:
              mensagem: Agente não encontrado
      securedBy: [JWT]
    delete:
      description: Deletar agente específico
      responses:
        200:
          body:
            type: Response
            example:
              mensagem: Agente deletado
        401:
          body:
            type: Response
            example:
              mensagem: Sem autorização
        404:
          body:
            type: Response
            example:
              mensagem: Agente não encontrado
      securedBy: [JWT]

  /{id}/events:
    get:
      description: Lista de eventos por agente
      responses:
        200:
          body:
            type: Event[]
        401:
          body:
            type: Response
            example:
              mensagem: Sem autorização
        404:
          body:
            type: Response
            example:
              mensagem: Não encontrado
      securedBy: [JWT]
    post:
      body: 
        application/json:
          example: {
              "event_id": 1,
              "agent_id": 1,
              "level": "level example",
              "data": "payload example",
              "shelve": true
            }
        201:
          body:
            type: Response
            example:
              mensagem: Lista criada
        401:
          body:
            type: Response
            example:
              mensagem: Sem autorização
        404:
          body:
            type: Response
            example:
              mensagem: Não encontrado agente
      securedBy: [JWT]
    put:
      description: Atualizar evento
      body:
        type: Event
        200:
          body:
            type: Response
            example:
              mensagem: Evento criado
        401:
          body:
            type: Response
            example:
              mensagem: Sem autorização
        404:
          body:
            type: Response
            example:
              mensagem: Não encontrado
      responses:
        200:
          body:
            type: Event
        400:
          body:
            type: Response
            example:
              mensagem: Solicitação inválida
      securedBy: [JWT]
    delete:
      description: Deletar evento
      body: 
        application/json:
          properties: 
            example: {
              }
        200:
          body:
            type: Response
            example:
              mensagem: Evento deletado
        401:
          body:
            type: Response
            example:
              mensagem: Sem autorização
        404:
          body:
            type: Response
            example:
              mensagem: Não encontrado
      responses:
        200:
          body:
            type: Response
            example:
              mensagem: Evento deletado
        401:
          body:
            type: Response
            example:
              mensagem: Sem autorização
        404:
          body:
            type: Response
            example:
              mensagem: Não encontrado
      securedBy: [JWT]

/groups:
  get:
    description: Lista de grupos
    responses:
      200:
        body:
          type: Group[]
      401:
        body:
          type: Response
          example:
            mensagem: Grupo não encontrado
    securedBy: [JWT]
  post:
    description: Criação de grupo
    body:
      application/json:
        properties: 
          example: {
              "group_id": 1,
              "name": "nome do grupo"
            }
        example: {
              "group_id": 1,
              "name": "nome do grupo"
            }
    responses:
      201:
        body:
          type: Group
      401:
        body:
          type: Response
          example:
            mensagem: Solicitação inválida
    securedBy: [JWT]

  /{id}:
    get:
      description: Detalhe do grupo
      responses:
        200:
          body:
            type: Group[]
        401:
          body:
            type: Response
            example:
              mensagem: Não autorizado
        404:
          body:
            type: Response
            example:
              mensagem: Não encontrado
      securedBy: [JWT]
    put:
      description: EDicação de um grupo
      body:
        type: Group
      responses:
        200:
          body:
            type: Group
        401:
          body:
            type: Response
            example:
              mensagem: Solicitação inválida
      securedBy: [JWT]
    delete:
      description: deletar um  grupo
      responses:
        204:
          body:
            type: Response
            example:
              mensagem: Excluído com sucesso
        400:
          body:
            type: Response
            example:
              mensagem: Solicitação inválida
      securedBy: [JWT]

/users:
  get:
    description: Lista de Usuários
    responses:
      200:
        body:
          type: User[]
    securedBy: [JWT]
  post:
    description: Criar usuário
    body:
      application/json:
        properties:
          example: {
              "user_id": 1,
              "name": "name",
              "email": "email",
              "last_login": "2019-11-20",
              "group_id": 1
            }
    responses:
      201:
        body:
          type: User
      401:
        body:
          type: Response
          example:
            mensagem: Sem autorização
      404:
        body:
          type: Response
          example:
            mensagem: Usuário não encontrado
    securedBy: [JWT]

  /{id}:
    get:
      description: Detalhe de Usuário
      responses:
        200:
          body:
            type: User[]
        401:
          body:
            type: Response
            example:
              mensagem: Não autorizado
        404:
          body:
            type: Response
            example:
              mensagem: Usuário não encontrado
      securedBy: [JWT]
    put:
      description: Editar usuário
      body:
        type: User
      responses:
        200:
          body:
            type: User
        401:
          body:
            type: Response
            example:
              mensagem: Sem autorização
        404:
          body:
            type: Response
            example:
              mensagem: Não encontrado
      securedBy: [JWT]
    delete:
      responses:
        200:
          body:
            type: Response
            example:
              mensagem: Excluído com sucesso
        401:
          body:
            type: Response
            example:
              mensagem: Sem autorização
        404:
          body:
            type: Response
            example:
              mensagem: Usuário não encontrado
      securedBy: [JWT]
'''
