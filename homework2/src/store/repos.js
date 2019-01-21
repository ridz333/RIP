import axios from 'axios';
import {sortBy} from 'lodash';

const LOAD_REPOS_SUCCESS = 'LOAD_REPOS_SUCCESS';
const LOAD_REPOS = 'LOAD_REPOS';
const url = 'https://forbes400.herokuapp.com/api/forbes400?limit=50'

const initialState = {
    isLoading: false,
    list: []
};

export const loadRepos = () => (dispatch) => {
    dispatch({
        type: LOAD_REPOS,
    });

    axios.get(url)
        .then(response => {
            dispatch({
                type: LOAD_REPOS_SUCCESS,
                payload: sortBy(response.data,'realTimeRank')
            })
        }).catch(() => {
            // Если ошибка, то будет пустой
            dispatch({
                type: LOAD_REPOS_SUCCESS,
                payload: []
            })
        });
};

function reducer(state = initialState, action) {
    switch (action.type) {
        case LOAD_REPOS:
            return Object.assign({}, state, {
                isLoading: true
            });
        case LOAD_REPOS_SUCCESS:
            return Object.assign({}, state, {
                list: action.payload,
                isLoading: false
            });
        default: return state;
    }
}

export default reducer;
