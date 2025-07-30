describe("Conversor de Moedas", () => {
  const userId = "cypress_user";

  beforeEach(() => {
    cy.visit("http://localhost:3000");
  });

  it("realiza uma conversão e mostra o resultado", () => {
    cy.get('input[placeholder="User ID"]').type(userId);

    cy.get('select').eq(0).select("USD");
    cy.get('select').eq(1).select("BRL");

    cy.get('input[type="number"]').clear().type("100");

    cy.contains("Converter").click();

    cy.contains("Resultado:").should("exist");
    cy.contains("BRL").should("exist");
  });

  it("consulta o histórico de transações", () => {
    cy.get('input[placeholder="User ID"]').type(userId);
    cy.contains("Ver Histórico").click();

    cy.contains("Histórico").should("exist");
    cy.get("div").contains("→").should("exist");
  });
});
