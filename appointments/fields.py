from django import forms

class ListTextWidget(forms.TextInput):
    def __init__(self, data_list, name, *args, **kwargs):
        super(ListTextWidget, self).__init__(*args, **kwargs)
        #store name in _name
        self._name = name
        #store data_list in _list
        self._list = data_list
        #set attributes to {'list:list_location_list'}
        self.attrs.update({'list':'list__%s' % self._name})

    def render(self, name, value, attrs=None, renderer=None):
        #create instance of ListTextWiget(derived from TextInput) and activate render method, and pass name, value, and attributes
        #store in text.html
        text_html = super(ListTextWidget, self).render(name, value, attrs=attrs)
        #data_list = <datalist id="list_location_list">
        data_list = '<datalist id="list__%s">' % self._name
        for item in self._list:
            #data_list = <datalist id="list_location_list"><option value=['address1']>...<option value=['addressn']>
            data_list += '<option value="%s">' % item
        #data_list = <datalist id="list_location_list"><option value=['address1']>...<option value=['addressn']></datalist>
        data_list += '</datalist>'

        return (text_html + data_list)
        #return(text_html + <datalist id="list_location_list"><option value=['address1']>...<option value=['addressn']></datalist>)
        #return(super(ListTextWidget, self).render(name, value, attrs=attrs) + <datalist id="list_location_list"><option value=['address1']>...<option value=['addressn']></datalist>)