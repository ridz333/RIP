import React,{ListGroup, Component} from 'react';
import axios from 'axios';
import Title from './content';
import InsideBlock from './inside';


class App extends Component{
    constructor(props){
        super(props)
        this.state = {
            repos: []
        }
    }
    componentDidMount(){
        axios.get('https://api.github.com/users/ridz333/repos').then(
            res => {
                console.log(res.data)
                this.setState({
                    repos: res.data
                })
            }
        )
    }
    render() {
        const { repos} = this.state
        
        return(
            repos.map( (el)=>{
                return(                            
                            <div key={el.id}>
                            <InsideBlock />
                                <a href={el.html_url} target="_blank">{el.name}</a>
                            </div>
                        )
            } )
        )
    };
}

export default App;