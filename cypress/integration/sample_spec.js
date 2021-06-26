describe('my first page load', () => {
  it('contains Hellow world!', () => {
    cy.visit('http://localhost:8080/')
    cy.contains("Hello world!")
  })
  
  it('can load the todo page', () => {
    cy.visit('http://localhost:8080/')
    cy.contains("Todo").click()
    cy.contains("Unable to connect to server")
  })
})
