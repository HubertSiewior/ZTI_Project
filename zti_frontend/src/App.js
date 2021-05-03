import React from 'react'
import {BrowserRouter} from 'react-router-dom'
import {Routing} from './Routing'
import {Provider} from "react-redux";
import createStore from "./redux/store"
import {Menu} from './components/Menu'


function App() {
    const store = createStore();
    // const color = "#53658a";
    return (
        <div>
            <Provider store={store}>
                <BrowserRouter>
                    <Menu/>
                    {/*<style>{`body { background-color: ${color}; }`}</style>*/}
                    <Routing/>
                </BrowserRouter>
            </Provider>
        </div>
    );
}

export default App;
