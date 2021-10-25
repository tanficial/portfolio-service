import React, { useState, useEffect } from "react";
import { Redirect, useHistory } from "react-router-dom";
import styled from "styled-components"

import { searchUsers } from "apis/searchApi"
import Message from "components/Message";
import ProfileCard from "components/ProfileCard";

const SearchMain = styled.main`
    min-height: calc(100vh - 80px);
    box-sizing: border-box;
    margin: 0 auto;
    padding: 80px 0;
    max-width: 960px;
    width: 100%;
`

const SearchWrapper = styled.div`
    width: 100%;
    position: relative;
    margin-bottom: 20px;
    padding: 0px 10px;
    box-sizing: border-box;
`

const InputSearch = styled.input`
    width: 100%;
    box-sizing: border-box;
    padding: 10px 80px 10px 10px;
    font-size: 16px;
    border: none;
    background-color: #F7F6F2;
`

const SearchButton = styled.button`
    height: 100%;
    width: 60px;
    position: absolute;
    top: 0;
    right: 10px;
    cursor: pointer;
    border: none;
    box-sizing: border-box;
    background-color: #C8C6C6;
    color: #222831;
    font-weight: bold;
    font-size: 16px;

    :hover {
        background-color: #4B6587;
        color: #F7F6F2;
    }
`

const UserList = styled.div`
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
`

const Search = ({ loginId, setLoginId }) => {
    const [query, setQuery] = useState("");
    const [users, setUsers] = useState(null);
    const history = useHistory();

    useEffect(() => {
        if (loginId === null) {
            return;
        }
        (async () => {
            try {
                const data = await searchUsers("");
                setUsers(data);
            } catch (e) {
                if (e.response.status === 401) {
                    alert("세션이 만료되었습니다.");
                    window.sessionStorage.clear();
                    setLoginId(null);
                    history.push("/login");
                }
            }
        })();
    }, [history, loginId, setLoginId]);

    const fetchUsersData = async () => {
        try {
            const data = await searchUsers(query);
            setUsers(data);
        } catch (e) {
            if (e.response.status === 401) {
                alert("세션이 만료되었습니다.");
                window.sessionStorage.clear();
                setLoginId(null);
                history.push("/login");
            }
        }
    }

    const handleCardClick = (userId) => {
        history.push(`/${userId}`);
    }

    const handleSearchButtonClick = () => {
        if (query.length < 2) {
            return alert("검색어는 최소 2글자 이상 입력해야 합니다.");
        }
        setUsers(null);
        fetchUsersData();
    }

    return (
        <SearchMain>
            {loginId === null && <Redirect to="/login" />}
            <SearchWrapper>
                <InputSearch value={query} onChange={e => setQuery(e.target.value)} />
                <SearchButton onClick={handleSearchButtonClick}>검색</SearchButton>
            </SearchWrapper>

            {
                users === null
                    ? <Message><h2>검색 중</h2></Message>
                    : (
                        users.length === 0
                            ? <Message><h2>검색 결과가 존재하지 않습니다.</h2></Message>
                            : <UserList>
                                {
                                    users.map(user =>
                                        <ProfileCard
                                            key={`user-search-card${user.id}`}
                                            onClick={handleCardClick}
                                            user={user}
                                            link={true}
                                        />
                                    )
                                }
                            </UserList>
                    )
            }
        </SearchMain>
    )
}

export default Search;