import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';

import './ListItem.css';

class ListItem extends Component {
    render() {
        const { repo } = this.props;
        const diff = repo.rank - repo.realTimeRank;
        let diffImgUrl = 'https://banner2.kisspng.com/20180430/ite/kisspng-computer-icons-equals-sign-clip-art-equal-sign-5ae773c6d18d26.5327001915251178948583.jpg'
        if (diff < 0)
            diffImgUrl = 'https://upload.wikimedia.org/wikipedia/commons/0/04/Red_Arrow_Down.svg'
        if (diff > 0)
            diffImgUrl = 'https://upload.wikimedia.org/wikipedia/commons/5/50/Green_Arrow_Up.svg'
            if (repo.squareImage){
                repo.squareImage = repo.squareImage.includes('http') ? `${repo.squareImage}` : `http:${repo.squareImage}`;
            }else{
                repo.squareImage = 'https://vk.com/images/deactivated_100.png?ava=1';
            }
            
            return (
            <div className='card' style={{display:'flex', marginTop: '20px', alignItems:'center', padding:'15px 20px'}}>
                <img style={{width:'76px', height:'76px', borderRadius: '38px'}} src={repo.squareImage}></img>
                <div style={{display:'flex', flexDirection:'column', marginLeft: '10px'}}>
                <div>Rank: {repo.realTimeRank} <img style={{width:'25px'}} src={diffImgUrl}></img></div>
                <div>Name: {repo.name}</div>
                <div>NetWorth: {repo.worth}M$</div>
                <div>Age: {repo.age}</div>
                <div>Company: {repo.source}</div>
                </div>
                
            </div>
            
        );
    }
}

export default ListItem;
