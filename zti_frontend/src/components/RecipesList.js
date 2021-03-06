import React, {useEffect, useState} from 'react'
import API from '../services/api'
import {Button, Col, Form, ListGroup, Row} from "react-bootstrap";
import {useHistory} from "react-router-dom";
import {useDispatch} from "react-redux";
import {showErrorPopup} from "../redux/actions";

const RecipeItem = (props) => {
    const icon = '🥪';
    const {id, dishName} = props;
    return <ListGroup.Item variant="primary" action href={`/recipe/${id}`}> {icon} {dishName}</ListGroup.Item>
};

export const RecipesList = () => {
    const dispatch = useDispatch();
    const history = useHistory();
    // if(JSON.parse(localStorage.getItem('user')) === null){
    //     history.push('/')
    // }
    const [recipes, setRecipes] = useState([]);
    const [filterName, setFilterName] = useState('');
    useEffect(() => {
        API.get(`/cookbook/recipe`)
            .then((response) => {
                console.log(response);
                setRecipes(response.data)
            })
        .catch(error => {
            dispatch(showErrorPopup(error.response.data))
        })
    }, [dispatch]);
    // const handleFilter = () => {
    //     API.get(`/recipe`, {
    //         params: {
    //             name: filterName
    //         }
    //     })
    //         .then((response) => {
    //             console.log(response);
    //             setRecipes(response.data)
    //         })
    //         .catch(error => {
    //             dispatch(showErrorPopup(error.response.data))
    //         })
    // };
    return (
        <Form>
            <Form.Group>
                <Col md={{span: 6, offset: 3}} sm={{span: 8, offset: 2}}>

                    <h4 className="card-header">Recipes list</h4>
                    <ListGroup>
                        {recipes.map((item) => <RecipeItem key={item.recipe_id}
                                                           id={item.recipe_id}
                                                           dishName={item.dish_name}/>)}
                    </ListGroup><br/>
                    <div className="text-center">
                        <Button href='/recipe/new' variant="success" className="mr-2 ">Add new recipe</Button>
                    </div>
                </Col>
            </Form.Group>
        </Form>
    )
};