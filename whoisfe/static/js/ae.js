let uiController=(function(){
    return{
        getInput(){
          return{
            type: document.querySelector(".add__henBoloh").value,
            description: document.querySelector(".add__ner").value,
            value: parseInt(document.querySelector(".add__Dugaar").value)
          };
        },
        addListItem: function(item,type){
          let html, list;
          if(type==='Uwuu','Emee','Aaw','Eej','Ah','Egch','Dvv','Naiz','Nuhur','Ehner' ){
            list='.FamilyInfo__list';
          html='<div class="item clearfix" id="FamilyInfo-%id%"><div class="item__ner">$$DESCRIPTION$$</div><div class="right clearfix"><div class="item__dugaar">$$VALUE$$</div><div class="item__delete">            <button class="add__btn">Nemeh</button></div>        </div></div>'
          }
          html=html.replace('%id%', item.henBoloh);
          html=html.replace('$$DESCRIPTION$$', item.ner);
          html=html.replace('$$VALUE$$', item.dugaar);
          document.querySelector(list).insertAdjacentHTML('beforeend', html);
  
        },
        clearFields:function(){
          let fields=document.querySelectorAll('.add__ner, .add__dugaar');
          let fieldArr=Array.prototype.slice.call(fields);
          fieldArr.forEach(function(){
            el.value='';
          });
          for(let i=0; i<fieldArr.length; i++){
            fieldArr[i].value='';
          }
          fieldArr[0].focus();
        }
      }
  
  })(uiController);