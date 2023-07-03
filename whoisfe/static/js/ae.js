let uiController = (function () {
  return {
    getInput() {
      return {
        henBoloh: document.querySelector(".add__henBoloh").value,
        ner: document.querySelector(".add__ner").value,
        dugaar: parseInt(document.querySelector(".add__dugaar").value)
      };
    },
    addListItem: function (item, henBoloh) {
      let html, list;
      if (id === 'henBoloh') {
        list = '.FamilyInfo__list';
        html = '<div class="item clearfix" id="FamilyInfo-%id%"><div class="item__ner">$$NER$$</div><div class="right clearfix"><div class="item__dugaar">$$DUGAAR$$</div><div class="item__delete">            <button class="item__delete--btn"><i class="ion-ios-close-outline"></i></button></div>        </div></div>'
      }
      html = html.replace('%id%', item.id);
      html = html.replace('$$NER$$', item.ner);
      html = html.replace('$$DUGAAR$$', item.dugaar);
      document.querySelector(list).insertAdjacentHTML('beforeend', html);

    },
    clearFields: function () {
      let fields = document.querySelectorAll('.add__ner, .add__dugaar');
      let fieldArr = Array.prototype.slice.call(fields);
      fieldArr.forEach(function () {
        el.value = '';
      });
      for (let i = 0; i < fieldArr.length; i++) {
        fieldArr[i].dugaar = '';
      }
      fieldArr[0].focus();
    }
  }

})();



let appController = (function (uiController) {
  let ctrlAddItem = function () {
    let input = uiController.getInput();
    let item = financeController.addItem(input.henBoloh, input.ner, input.dugaar);
    uiController.addListItem(item, input.henBoloh);
  };
  document.querySelector(".add__btn").addEventListener("click", function () {
    ctrlAddItem();
  });

  document.addEventListener("keypress", function (event) {
    if (event.keyCode === 13 || event.which === 13) {
      ctrlAddItem();
    }
  });
})(uiController);